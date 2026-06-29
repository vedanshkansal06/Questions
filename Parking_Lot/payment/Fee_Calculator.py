import math
from payment.Parking_Rate import ParkingRate
from models.Parking_Ticket import ParkingTicket

class FeeCalculator:
    def __init__(self, parking_rate: ParkingRate):
        self.parking_rate = parking_rate

    def calculate_fee(self, ticket: ParkingTicket):
        if not ticket.exit_time:
            raise ValueError("Ticket has no exit time")
        duration = ticket.exit_time - ticket.entry_time
        total_hours = math.ceil(duration.total_seconds() / 3600)
        if total_hours <= 0:
            raise ValueError("Total hours exceeds 0")
        fee = 0.0
        for hour in range(1, int(total_hours) + 1):
            if hour == 1:
                fee += self.parking_rate.hour_1
            elif hour == 2 or hour == 3:
                fee += self.parking_rate.hour_2_3
            else:
                fee += self.parking_rate.hour_remaining
        return fee