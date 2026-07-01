class Account:
    def __init__(self):
        self.active_lendings = []
        self.reservations = []
        self.fine_balance = 0.0

    def count_active_lendings(self):
        return len(self.active_lendings)

    def add_fine(self, amount: float):
        self.fine_balance += amount

    def pay_fine(self, amount: float):
        if amount > self.fine_balance:
            self.fine_balance = amount
        self.fine_balance -= amount