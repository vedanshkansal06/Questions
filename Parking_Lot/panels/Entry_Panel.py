from typing import Optional
from core.Parking_Lot import ParkingLot
from models.Vehicle import Vehicle
from models.Parking_Ticket import ParkingTicket

class EntryPanel:
    def __init__(self, panel_id: str) -> None:
        self.panel_id = panel_id

    def process_entry(self, vehicle: Vehicle) -> Optional[ParkingTicket]:
        parking_lot = ParkingLot.get_instance()
        parking_lot.recalculate_capacity()
        if parking_lot.is_full():
            print(f"Entry Panel {self.panel_id}: Parking Lot Full")
            return None
        spot = parking_lot.get_available_spot(vehicle)
        if not spot:
            print(f"Entry Panel {self.panel_id}: No Compatible Spot Available for {vehicle.get_type().name}")
        ticket = ParkingTicket(vehicle.registration_number, spot.spot_id)
        floor = parking_lot.get_floor_by_spot(spot.spot_id)
        if floor:
            floor.mark_spot_occupied(spot.spot_id, vehicle)
            parking_lot.increase_occupancy()
            print(f"Entry Panel {self.panel_id}: Issued ticket {ticket.ticket_id} for spot {spot.spot_id}")
            return ticket
        return None
