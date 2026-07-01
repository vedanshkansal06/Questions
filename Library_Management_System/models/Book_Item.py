from typing import Optional
from datetime import date
from States import BookStatus
from Exceptions import safe_transition
from models.Books import Book
from models.Rack import Rack

class BookItem:
    def __init__(self, barcode: str, rack: Rack):
        self.barcode = barcode
        self.status = BookStatus.Available
        self.rack = rack
        self.date: Optional[date] = None
        self.book = None

    def set_book(self, book: Book):
        self.book = book

    def reserve_book(self):
       safe_transition(self.status, BookStatus.Reserved, [BookStatus.Available])
       self.status = BookStatus.Reserved

    def check_out_book(self):
        safe_transition(self.status, BookStatus.Loaned, [BookStatus.Reserved, BookStatus.Available])
        self.status = BookStatus.Loaned

    def return_book(self):
        safe_transition(self.status, BookStatus.Available, [BookStatus.Loaned])
        self.status = BookStatus.Available

    def report_lost(self):
        safe_transition(self.status, BookStatus.Lost, [BookStatus.Loaned])
        self.status = BookStatus.Lost

