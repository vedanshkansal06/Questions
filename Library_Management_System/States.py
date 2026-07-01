from enum import Enum, auto

class BookStatus(Enum):
    Available = auto()
    Reserved = auto()
    Loaned = auto()
    Lost = auto()
    Unavailable = auto()

class ReservationStatus(Enum):
    Waiting = auto()
    Pending = auto()
    Completed = auto()
    Cancelled = auto()

class MemberStatus(Enum):
    Active = auto()
    Blacklisted = auto()
    Cancelled = auto()

class LendingStatus(Enum):
    Active = auto()
    Returned = auto()
    Renewed = auto()
