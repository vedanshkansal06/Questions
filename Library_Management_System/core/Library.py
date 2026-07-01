from typing import List, Optional, TYPE_CHECKING
from transactions.Book_Lending import BookLending
from transactions.Book_Reservation import BookReservation
from transactions.Fine import Fine
from search.Catalog import Catalog

if TYPE_CHECKING:
    from models.Person import Member, Librarian

class Library:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Library, cls).__new__(cls)
        return cls._instance

    def __init__(self, catalog: Catalog = None, notification_service = None):
        if getattr(self, '_initialized', False):
            return
        self.catalog = catalog
        self.notification_service = notification_service
        self.members: List[Member] = []
        self.librarian: List[Librarian] = []
        self.book_lending: List[BookLending] = []
        self.book_reservation: List[BookReservation] = []
        self.fine: List[Fine] = []
        self.FINE_THRESHOLD = 10.0
        self._initialized = True

    def add_librarian(self, librarian: 'Librarian'):
        self.librarian.append(librarian)

    def get_librarian(self, employee_id: str) -> Optional['Librarian'] :
        for lib in self.librarian:
            if lib.employee_id == employee_id:
                return lib
        return None

    def get_member(self, member_barcode: str) -> Optional['Member'] :
        for m in self.members:
            if m.library_card.barcode == member_barcode:
                return m
        return None
