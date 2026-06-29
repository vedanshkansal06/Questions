import datetime
from states import TicketStatus

class ParkingTicket:
    _id_counter = 1

    def __init__(self, vehicle_registration_number: str, spot_number:str):
        self.ticket_id = f"TKT: {ParkingTicket._id_counter:03d}"
        self.vehicle_registration_number = vehicle_registration_number
        self.spot_number = spot_number
        self.entry_time = datetime.datetime.now()
        self.exit_time = None
        self.status = TicketStatus.Active

    def mark_paid(self):
        self.status = TicketStatus.Paid

    def mark_exit_time(self):
        self.exit_time = datetime.datetime.now()

    def report_lost(self):
        self.status = TicketStatus.Lost