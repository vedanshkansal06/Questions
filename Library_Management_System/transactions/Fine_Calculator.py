from datetime import date

from transactions.Book_Lending import BookLending
from transactions.Fine import Fine

class FineCalculator:
    Fine_Charge_Per_Day = 2

    @staticmethod
    def calculate_fine(book_lending: BookLending, current_date: date):
        if book_lending.due_date >= current_date:
            return None
        return FineCalculator.Fine_Charge_Per_Day * (current_date - book_lending.due_date).days

    @staticmethod
    def apply_fine(book_lending: BookLending, current_date: date):
        amount = FineCalculator.calculate_fine(book_lending, current_date)
        if amount is not None and amount > 0:
            return Fine(book_lending, book_lending.member_barcode, amount)
        return 0
