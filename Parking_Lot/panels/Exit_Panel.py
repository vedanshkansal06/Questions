from states import TicketStatus, PaymentStatus
from models.Parking_Ticket import ParkingTicket
from core.Parking_Lot import ParkingLot
from payment.Fee_Calculator import FeeCalculator
from payment.Payment_Strategy import PaymentStrategy

class ExitPanel:
    def __init__(self, panel_id, fee_calculator: FeeCalculator):
        self.panel_id = panel_id
        self.fee_calculator = fee_calculator

    def process_exit(self, ticket: ParkingTicket, payment_strategy: PaymentStrategy):
        print(f"Exit Panel {self.panel_id}: Processing ticket {ticket.ticket_id}")
        parking_lot = ParkingLot.get_instance()
        if ticket.status == TicketStatus.Active:
            ticket.mark_exit_time()
            fee = self.fee_calculator.calculate_fee(ticket)
            if fee > 0:
                if not payment_strategy:
                    print("Please Enter Payment Strategy first")
                    return False
                payment_status = payment_strategy.pay(fee)
                if payment_status != PaymentStatus.Success:
                    print(f"Exit Panel {self.panel_id}: Payment Status is Failed.")
                    return False
            ticket.mark_paid()
            print(f"Exit Panel {self.panel_id}: Payment Status is Success.")
        elif ticket.status == TicketStatus.Paid:
            print(f"Exit Panel {self.panel_id}: Payment Already Paid.")
        else:
            print(f"Exit Panel {self.panel_id}: Invalid Ticket Status.")
            return False
        floor = parking_lot.get_floor_by_spot(ticket.spot_number)
        if floor:
            floor.mark_spot_free(ticket.spot_number)
            parking_lot.decrease_occupancy()
            print(f"Exit Panel {self.panel_id}: Spot {ticket.spot_number}Free.")
            return True
        return False
