from abc import ABC, abstractmethod
from states import PaymentStatus

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> PaymentStatus:
        pass

class Cash(PaymentStrategy):
    def pay(self, amount: float) -> PaymentStatus:
        print(f"Processing Cash Payment of {amount:.2f}")
        return PaymentStatus.Success

class CreditCard(PaymentStrategy):
    def pay(self, amount: float) -> PaymentStatus:
        print(f"Processing Credit Card Payment of {amount:.2f}")
        return PaymentStatus.Success