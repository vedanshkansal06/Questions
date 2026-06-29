from abc import ABC
from core.Parking_Lot import ParkingLot
from core.Parking_Floor import ParkingFloor
from models.Parking_Spot import ParkingSpot
from payment.Parking_Rate import ParkingRate

class Person(ABC):
    def __init__(self, name: str):
        self.name = name

class Customer(Person):
    def __init__(self, name: str):
        super().__init__(name)

class ParkingAttendant(Person):
    def __init__(self, name: str):
        super().__init__(name)

class Admin(Person):
    def __init__(self, name: str):
        super().__init__(name)

    def add_parking_floor(self, floor: ParkingFloor):
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_floor(floor)
        print(f"Admin {self.name} Added {floor.floor_number} Floor Successfully.")

    def modify_parking_floor(self, old_floor_number: str, new_floor_number: str):
        parking_lot = ParkingLot.get_instance()
        if old_floor_number in parking_lot.floors:
            parking_lot.modify_floor(old_floor_number, new_floor_number)
            print(f"Admin {self.name} Modified Floor Successfully.")
        else:
            print(f"Floor {old_floor_number} not found.")

    def remove_parking_floor(self, floor_number: str):
        parking_lot = ParkingLot.get_instance()
        if floor_number in parking_lot.floors:
            parking_lot.remove_floor(floor_number)
            print(f"Admin {self.name} Removed Floor Successfully.")
        else:
            print(f"Floor {floor_number} not found.")

    def add_parking_spot(self, floor_number: str, spot: ParkingSpot):
        parking_lot = ParkingLot.get_instance()
        if floor_number in parking_lot.floors:
            parking_lot.floors[floor_number].add_spot(spot)
            parking_lot.recalculate_capacity()
            print(f"Admin {self.name} Added Spot Successfully.")
        else:
            print(f"Floor {floor_number} not found.")

    def modify_parking_spot(self, floor_number: str, old_spot_number: str, new_spot: ParkingSpot):
        parking_lot = ParkingLot.get_instance()
        if floor_number in parking_lot.floors:
            floor = parking_lot.floors
            if old_spot_number in floor.spots:
                floor.remove_spot(old_spot_number)
                floor.add_spot(new_spot)
                parking_lot.recalulate_capacity()
                print(f"Admin {self.name} Modified Spot Successfully.")
            else:
                print(f"Floor {old_spot_number} not found.")
        else:
            print(f"Floor {floor_number} not found.")

    def remove_parking_spot(self, floor_number: str, spot_number: str):
        parking_lot = ParkingLot.get_instance()
        if floor_number in parking_lot.floors:
            floor = parking_lot.floors[floor_number]
            if spot_number in floor.spots:
                floor.remove_spot(spot_number)
                parking_lot.recalulate_capacity()
                print(f"Admin {self.name} Removed Spot Successfully.")
            else:
                print(f"Spot: {spot_number} not found.")
        else:
            print(f"Floor {floor_number} not found.")

    def add_attendant(self, parking_attendant: ParkingAttendant):
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_attendant(parking_attendant)
        print("Admin Added Attendant Successfully.")

    def remove_attendant(self, parking_attendant: str):
        parking_lot = ParkingLot.get_instance()
        parking_lot.remove_attendant(parking_attendant)
        print("Admin Remove Attendant Successfully.")

    def update_parking_rate(self, parking_rate: ParkingRate, new_hour_1: float, new_hour_2_3: float, new_hour_remaining: float):
        parking_rate.hour_1 = new_hour_1
        parking_rate.hour_2_3 = new_hour_2_3
        parking_rate.hour_remaining = new_hour_remaining
