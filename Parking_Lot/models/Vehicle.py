from abc import ABC,abstractmethod
from states import VehicleType

class Vehicle(ABC):
    def __init__(self, registration_number):
        self.registration_number = registration_number

    @abstractmethod
    def get_type(self) -> VehicleType: pass

class Bike(Vehicle):
    def get_type(self) -> VehicleType: return VehicleType.Bike

class Car(Vehicle):
    def get_type(self) -> VehicleType: return VehicleType.Car

class Truck(Vehicle):
    def get_type(self) -> VehicleType: return VehicleType.Truck

class Van(Vehicle):
    def get_type(self) -> VehicleType: return VehicleType.Van

class Electric(Vehicle):
    def get_type(self) -> VehicleType: return VehicleType.Electric