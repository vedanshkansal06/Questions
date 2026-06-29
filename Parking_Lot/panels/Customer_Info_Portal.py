from models.Parking_Ticket import ParkingTicket
from payment.Payment_Strategy import PaymentStrategy
from payment.Fee_Calculator import FeeCalculator
from states import TicketStatus, PaymentStatus

class CustomerInfoPortal:
    def __init__(self, portal_id: str, fee_calculator: FeeCalculator):
        self.portal_id = portal_id
        self.fee_calculator = fee_calculator

    def process_payment(self,ticket:ParkingTicket, payment_strategy: PaymentStrategy):
        print(f"Info Portal {self.portal_id}: Processing Ticket {ticket.ticket_id}")
        if ticket.status == TicketStatus.Paid:
            print("Ticket Status: Already Paid")
            return True
        if ticket.status != TicketStatus.Active:
            print("Invalid Ticket Status.")
            return False
        ticket.mark_exit_time()
        fee = self.fee_calculator.calculate_fee(ticket)
        print(f"Amount To Be Paid: ${fee:.2f}")
        if fee > 0:
            payment_status = payment_strategy.pay(fee)
            if payment_status != PaymentStatus.Success:
                print("Payment Status: Payment Failed.")
                return False
        ticket.mark_paid()
        print(f"Ticket Status: Paid Successfully {ticket.ticket_id}")
        return True