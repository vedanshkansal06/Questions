from enum import Enum, auto

class VehicleType(Enum):
    Bike = auto()
    Car = auto()
    Truck = auto()
    Van = auto()
    Electric = auto()

class SpotType(Enum):
    Bike = auto()
    Compact = auto()
    Large = auto()
    Electric = auto()
    Handicapped = auto()

class TicketStatus(Enum):
    Paid = auto()
    Active = auto()

class PaymentType(Enum):
    Cash = auto()
    CreditCard = auto()

class PaymentStatus(Enum):
    Unpaid = auto()
    Success = auto()