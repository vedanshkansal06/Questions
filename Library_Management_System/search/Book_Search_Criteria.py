from models.Books import Book
class BookSearchCriteria:
    def __init__(self, title = None , author = None, subject = None, publication_date = None):
        self.title = title
        self.author = author
        self.subject = subject
        self.publication_date = publication_date

    def matches(self, book: Book):
        if self.title and self.title.lower() not in book.title.lower():
            return False
        if self.author:
            author_match = False
            for auth in book.authors:
                if self.author.lower() == auth.name.lower():
                    author_match = True
                    break
            if not author_match:
                return False
        if self.subject and self.subject.lower() != book.subject.lower():
            return False
        if self.publication_date and self.publication_date.lower() != book.publication_date.lower():
            return False
        return True

