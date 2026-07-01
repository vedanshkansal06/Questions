from typing import List, Optional
from models.Books import Book
from search.Book_Search_Criteria import BookSearchCriteria

class Catalog:
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        self.books.remove(book)

    def search_book(self, criteria: BookSearchCriteria) -> List[Book]:
        return [item for item in self.books if criteria.matches(item)]

    def get_book_by_isbn(self, isbn: int) -> Optional[Book]:
        for book in self.books:
            if book.ISBN == isbn:
                return book
        return None
