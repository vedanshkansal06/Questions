from dataclasses import dataclass
from datetime import date

@dataclass
class LibraryCard:
    barcode: str
    issue_date: date
    active: bool = True