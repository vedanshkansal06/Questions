from datetime import date, timedelta

from models.Author import Author
from models.Rack import Rack
from models.Book_Item import BookItem
from models.Books import Book
from models.Library_Card import LibraryCard
from models.Account import Account
from States import MemberStatus, ReservationStatus, BookStatus, LendingStatus
from core.Library import Library
from Exceptions import MemberNotActiveError, CheckOutLimitError, BookNotAvailableError
from transactions.Book_Lending import BookLending
from transactions.Book_Reservation import BookReservation
from transactions.Fine_Calculator import FineCalculator


class Person:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone


def _find_book_item(catalog, book_item_barcode):
    for book in catalog.books:
        for item in book.book_items:
            if item.barcode == book_item_barcode:
                return item
    return None

def _get_active_lending_for_book_item(lendings, book_item_barcode):
    for lending in lendings:
        if lending.book_item.barcode == book_item_barcode and lending.status in [LendingStatus.Active, LendingStatus.Renewed]:
            return lending
    return None

class Member(Person):
    def __init__(self, name: str, phone: str, library_card: LibraryCard):
        super().__init__(name, phone)
        self.library_card = library_card
        self.account = Account()
        self.state = MemberStatus.Active

    def reserve_book(self, isbn: int, current_date: date):
        library = Library()
        if self.state != MemberStatus.Active:
            raise MemberNotActiveError("Member is not active!!")
        if self.account.count_active_lendings() >=5:
            raise CheckOutLimitError("Checkout limit exceeded!!")
        book = library.catalog.get_book_by_isbn(isbn)
        if not book:
            raise ValueError("Book not found!!")
        for reservation in self.account.reservations:
            if reservation.book == book and reservation.status in [ReservationStatus.Waiting, ReservationStatus.Pending]:
                raise ValueError("Reservation already exists!!")
        reservation = BookReservation(self.library_card.barcode, book, current_date)
        library.book_reservation.append(reservation)
        self.account.reservations.append(reservation)
        if len(book.get_available_books()) > 0:
            available_copy = book.get_available_books()[0]
            reservation.activate()
            available_copy.reserve_book()
            library.notification_service.notify(self, f"Your reserved book '{book.title}' is available immediately for pickup.")
        return reservation

    def checkout_book(self, book_item_barcode: str, current_date: date):
        library = Library()
        if self.state != MemberStatus.Active:
            raise MemberNotActiveError("Member is not active!!")
        if self.account.count_active_lendings() >=5:
            raise CheckOutLimitError("Checkout limit exceeded!!")
        book_item = _find_book_item(library.catalog, book_item_barcode)
        if not book_item:
            raise ValueError("Book item not found!!")
        if book_item.status not in [BookStatus.Available, BookStatus.Reserved]:
            raise BookNotAvailableError("Book is not available!!")
        if book_item.status == BookStatus.Reserved:
            matching_reservation = None
            for reservation in library.book_reservation:
                if reservation.status == ReservationStatus.Pending and reservation.book == book_item.book and reservation.member_barcode == self.library_card.barcode:
                    matching_reservation = reservation
                    break
            if not matching_reservation:
                raise BookNotAvailableError("Book is not available!!")
            matching_reservation.complete()
        for lending in self.account.active_lendings:
            if lending.book_item.book == book_item.book:
                raise ValueError("Member already has a copy!!")
        book_item.check_out_book()
        new_lending = BookLending(book_item, self.library_card.barcode, current_date)
        library.book_lending.append(new_lending)
        self.account.active_lendings.append(new_lending)
        return new_lending

    def renew_book(self, book_item_barcode: str, current_date: date):
        library = Library()
        if self.state != MemberStatus.Active:
            raise MemberNotActiveError("Member is not active!!")
        active_lending = None
        for lending in self.account.active_lendings:
            if lending.book_item.barcode == book_item_barcode:
                active_lending = lending
                break
        if not active_lending:
            raise ValueError("Book not found!!")
        if active_lending.renewals >= 1:
            raise ValueError("Renewal limit exceeded!!")
        book = active_lending.book_item.book
        for reservation in library.book_reservation:
            if reservation.book == book and reservation.status == ReservationStatus.Waiting:
                raise ValueError("Reservation already exists!!")
        active_lending.due_date =current_date + timedelta(days=10)
        active_lending.renewals += 1
        active_lending.status = LendingStatus.Renewed

    def return_book(self, book_item_barcode: str, current_date: date):
        library = Library()
        active_lending = _get_active_lending_for_book_item(library.book_lending, book_item_barcode)
        if not active_lending:
            raise ValueError("No active lending found!!")
        if self.state != MemberStatus.Active:
            raise MemberNotActiveError("Member is not active!!")
        member = library.get_member(active_lending.member_barcode)
        fine = FineCalculator.apply_fine(active_lending, current_date)
        if fine:
            library.fine.append(fine)
            member.account.add_fine(fine.amount)
            if member.account.fine_balance >= library.FINE_THRESHOLD:
                member.state = MemberStatus.Blacklisted
        active_lending.status = LendingStatus.Returned
        active_lending.return_date = current_date
        member.account.active_lendings.remove(active_lending)
        book_item = active_lending.book_item
        book_item.return_book()
        book = book_item.book
        waiting_reservation = [reservation for reservation in library.book_reservation if reservation.book == book and reservation.status == ReservationStatus.Waiting]
        if waiting_reservation:
            first_reservation = sorted(waiting_reservation, key=lambda x: x.reservation_date)[0]
            first_reservation.activate()
            book_item.reserve_book()
            reserver = library.get_member(first_reservation.member_barcode)
            library.notification_service.notify(reserver, f"Book with title {book.title} is now available for pickup.")


class Librarian(Member):
    def __init__(self, name: str, phone: str,library_card:LibraryCard, employee_id: str):
        super().__init__(name, phone, library_card)
        self.employee_id = employee_id

    def add_member(self, member: Member):
        library = Library()
        library.members.append(member)

    def cancel_member(self, member_barcode: str):
        library = Library()
        member = library.get_member(member_barcode)
        if member:
            member.status = MemberStatus.Cancelled

    def add_book(self, isbn: int, title:str, subject: str, publication_date:str, authors: list):
        library = Library()
        book = Book(isbn, title, subject, publication_date)
        for name in authors:
            name = Author(name)
            book.add_author(name)
        library.catalog.books.append(book)

    def edit_book(self, isbn: int, title: str = None, subject: str = None, publication_date: str = None):
        library = Library()
        book = library.catalog.get_book_by_isbn(isbn)
        if book:
            if title and title != "": book.title = title
            if subject and subject != "": book.subject = subject
            if publication_date and publication_date != "": book.publication_date = publication_date
        return book

    def remove_book(self, isbn: int):
        library = Library()
        book = library.catalog.get_book_by_isbn(isbn)
        library.catalog.remove_book(book)

    def add_book_item(self, isbn: int, barcode: str, rack: Rack):
        library = Library()
        book =  library.catalog.get_book_by_isbn(isbn)
        if not book:
            raise ValueError("Book not found!!")
        book_item = BookItem(barcode, rack)
        book.add_book_item(book_item)

    def edit_book_item(self, isbn: int, barcode: str, rack: Rack):
        library = Library()
        book =  library.catalog.get_book_by_isbn(isbn)
        if book:
            for book_item in book.book_items:
                if book_item.barcode == barcode:
                    book_item.rack = rack
                return book_item
        return None

    def remove_book_item(self, isbn: int, barcode: str):
        library = Library()
        book = library.catalog.get_book_by_isbn(isbn)
        if book:
            for book_item in book.book_items:
                if book_item.barcode == barcode:
                    book_item.status = BookStatus.Unavailable
                    break
