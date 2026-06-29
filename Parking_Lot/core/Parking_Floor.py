from typing import Dict, Optional
from states import SpotType
from models.Parking_Spot import ParkingSpot
from models.Vehicle import Vehicle
from core.Display_Board import DisplayBoard

class ParkingFloor:
    def __init__(self, floor_number: str):
        self.floor_number = floor_number
        self.spots : Dict[str, ParkingSpot] = {}
        self.display_board = DisplayBoard()
        self._update_display_board()

    def _update_display_board(self):
        counts = {
            SpotType.Compact : 0,
            SpotType.Large : 0,
            SpotType.Bike : 0,
            SpotType.Handicapped : 0,
            SpotType.Electric : 0
        }
        for spot in self.spots.values():
            if spot.is_available:
                counts[spot.spot_type] += 1
        for spot_type, count in counts.items():
            self.display_board.update_count(spot_type, count)

    def add_spot(self,spot: ParkingSpot):
        self.spots[spot.spot_id] = spot
        self._update_display_board()

    def remove_spot(self,spot_id: str):
        if spot_id in self.spots:
            del self.spots[spot_id]
            self._update_display_board()

    def get_available_spot(self,vehicle: Vehicle) -> Optional[ParkingSpot]:
        for spot in self.spots.values():
            if spot.is_available and spot.is_vehicle_compatible(vehicle):
                return spot
        return None

    def mark_spot_occupied(self, spot_id: str, vehicle: Vehicle):
        if spot_id in self.spots:
            spot = self.spots[spot_id]
            spot.park_vehicle(vehicle)
            self._update_display_board()

    def mark_spot_free(self, spot_id: str):
        if spot_id in self.spots:
            spot = self.spots[spot_id]
            spot.remove_vehicle()
            self._update_display_board()

