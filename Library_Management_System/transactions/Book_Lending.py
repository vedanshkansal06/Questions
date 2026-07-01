from datetime import date, timedelta
from typing import Optional
from States import LendingStatus
from models.Book_Item import BookItem

class BookLending:
    def __init__(self, book_item: BookItem, member_barcode: str, lending_date: date):
        self.book_item = book_item
        self.member_barcode = member_barcode
        self.lending_date = lending_date
        self.due_date = self.lending_date + timedelta(days=10)
        self.return_date: Optional[date] = None
        self.status = LendingStatus.Active
        self.renewals = 0
