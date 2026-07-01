from typing import List, TYPE_CHECKING
from States import BookStatus
from models.Author import Author

if TYPE_CHECKING:
    from models.Book_Item import BookItem

class Book:
    def __init__(self,isbn: int, title: str,subject:str,publication_date: str):
        self.ISBN = isbn
        self.title =title
        self.subject = subject
        self.publication_date = publication_date
        self.authors: list[Author] = []
        self.book_items: list['BookItem'] = []

    def add_book_item(self, book_item: 'BookItem'):
        book_item.set_book(self)
        self.book_items.append(book_item)

    def add_author(self, author: Author):
        self.authors.append(author)

    def get_available_books(self) -> List['BookItem']:
        return [item for item in self.book_items if item.status == BookStatus.Available]

