from transactions.Book_Lending import BookLending

class Fine:
    def __init__(self, book_lending: BookLending, member_barcode: str, amount: float):
        self.book_lending = book_lending
        self.member_barcode = member_barcode
        self.amount = amount
        self.paid = False