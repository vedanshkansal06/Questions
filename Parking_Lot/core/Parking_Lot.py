from typing import Dict, Optional
from core.Parking_Floor import ParkingFloor
from models.Vehicle import Vehicle
from models.Parking_Spot import ParkingSpot

class ParkingLot:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ParkingLot, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def _initialize(self):
        self.floors: Dict[str, ParkingFloor] = {}
        self.entry_panels = []
        self.exit_panels = []
        self.attendants = {}
        self.capacity = 0
        self.occupied_count = 0

    def add_attendant(self, attendant):
        self.attendants[attendant.name] = attendant

    def remove_attendant(self, attendant_name: str):
        if attendant_name in self.attendants:
            del self.attendants[attendant_name]

    def add_entry_panel(self, panel):
        self.entry_panels.append(panel)

    def add_exit_panel(self, panel):
        self.exit_panels.append(panel)

    def add_floor(self, floor: ParkingFloor):
        self.floors[floor.floor_number] = floor
        self.recalculate_capacity()

    def modify_floor(self, old_floor:str, new_floor: str):
        if old_floor in self.floors:
            floor = self.floors.pop(old_floor)
            floor.floor_number = new_floor
            self.floors[new_floor] = floor

    def remove_floor(self, floor_number: str):
        if floor_number in self.floors:
            del self.floors[floor_number]
            self.recalculate_capacity()

    def recalculate_capacity(self):
        self.capacity = sum(len(floor.spots) for floor in self.floors.values())

    def get_available_spots(self,vehicle: Vehicle) -> Optional[ParkingSpot]:
        for floor in self.floors.values():
            spot = floor.get_available_spot(vehicle)
            if spot:
                return spot
        return None

    def is_full(self) -> bool:
        return self.occupied_count >= self.capacity

    def increase_occupancy(self):
        self.occupied_count += 1

    def decrease_occupancy(self):
        if self.occupied_count > 0:
            self.occupied_count -= 1

    def get_floor_by_spot(self, spot_number: str) -> Optional[ParkingFloor]:
        for floor in self.floors.values():
            if spot_number in floor.spots:
                return floor
        return None