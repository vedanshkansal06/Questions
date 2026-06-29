from abc import ABC, abstractmethod
from typing import Optional
from models.Vehicle import Vehicle, VehicleType
from states import SpotType


class ParkingSpot(ABC):
    def __init__(self, spot_id: str, spot_type: SpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self._is_available = True
        self.parked_vehicle: Optional[Vehicle] = None

    @abstractmethod
    def is_vehicle_compatible(self, vehicle) -> bool: pass

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        if self.is_available and self.is_vehicle_compatible(vehicle):
            self.parked_vehicle = vehicle
            self._is_available = False
            return True
        return False

    def remove_vehicle(self) -> None:
        self.parked_vehicle = None
        self._is_available = True

    @property
    def is_available(self) -> bool:
        return self._is_available

class CompactSpot(ParkingSpot):
    def __init__(self, spot_id: str):
        super().__init__(spot_id, SpotType.Compact)

    def is_vehicle_compatible(self, vehicle: Vehicle) -> bool:
        return vehicle.get_type() in [VehicleType.Car]

class LargeSpot(ParkingSpot):
    def __init__(self, spot_id: str):
        super().__init__(spot_id, SpotType.Large)

    def is_vehicle_compatible(self, vehicle: Vehicle) -> bool:
        return vehicle.get_type() in [VehicleType.Car, VehicleType.Truck, VehicleType.Van]

class BikeSpot(ParkingSpot):
    def __init__(self, spot_id: str):
        super().__init__(spot_id, SpotType.Bike)

    def is_vehicle_compatible(self, vehicle: Vehicle) -> bool:
        return vehicle.get_type() in [VehicleType.Bike]

class HandicappedSpot(ParkingSpot):
    def __init__(self, spot_id: str):
        super().__init__(spot_id, SpotType.Handicapped)

    def is_vehicle_compatible(self, vehicle: Vehicle) -> bool:
        return vehicle.get_type() in [VehicleType.Car, VehicleType.Van]

class ElectricSpot(ParkingSpot):
    def __init__(self, spot_id: str):
        super().__init__(spot_id, SpotType.Electric)

    def is_vehicle_compatible(self, vehicle: Vehicle) -> bool:
        return vehicle.get_type() in [VehicleType.Electric]