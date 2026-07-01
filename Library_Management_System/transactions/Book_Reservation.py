from datetime import date
from States import ReservationStatus
from models.Books import Book
from Exceptions import safe_transition

class BookReservation:
    def __init__(self,member_barcode: str, book: Book, reservation_date: date):
        self.member_barcode = member_barcode
        self.book = book
        self.reservation_date = reservation_date
        self.status = ReservationStatus.Waiting

    def activate(self):
        safe_transition(self.status, ReservationStatus.Pending, [ReservationStatus.Waiting])
        self.status = ReservationStatus.Pending

    def complete(self):
        safe_transition(self.status, ReservationStatus.Completed, [ReservationStatus.Pending])
        self.status = ReservationStatus.Completed

    def cancel(self):
        safe_transition(self.status, ReservationStatus.Cancelled, [ReservationStatus.Waiting, ReservationStatus.Pending])
        self.status = ReservationStatus.Cancelled
