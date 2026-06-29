from states import SpotType

class DisplayBoard:
    def __init__(self):
        self.count = {
            SpotType.Compact: 0,
            SpotType.Large: 0,
            SpotType.Bike: 0,
            SpotType.Handicapped: 0,
            SpotType.Electric: 0
        }

    def update_count(self, spot_type: SpotType, count: int):
        self.count[spot_type] = count
    
    def show_board(self, is_lot_full: bool = False):
        if is_lot_full:
            print("Parking Lot Full!!!")
        print("Display Board")
        for spot_type, count in self.count.items():
            print(f"{spot_type}: {count}")