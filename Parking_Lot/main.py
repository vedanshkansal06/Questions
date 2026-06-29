import datetime
from core.Parking_Lot import ParkingLot
from core.Parking_Floor import ParkingFloor
from models.Parking_Spot import CompactSpot, LargeSpot, BikeSpot, ElectricSpot, HandicappedSpot
from models.Vehicle import Car, Truck, Bike, Electric, Van
from payment.Parking_Rate import ParkingRate
from payment.Fee_Calculator import FeeCalculator
from payment.Payment_Strategy import Cash, CreditCard
from panels.Entry_Panel import EntryPanel
from panels.Exit_Panel import ExitPanel
from panels.Customer_Info_Portal import CustomerInfoPortal
from models.Person import Admin, ParkingAttendant

def initialize_parking_lot():
    parking_lot = ParkingLot()
    floor_1 = ParkingFloor("F-1")
    floor_1.add_spot(CompactSpot("F1-C1"))
    floor_1.add_spot(CompactSpot("F1-C2"))
    floor_1.add_spot(LargeSpot("F1-L1"))
    floor_1.add_spot(BikeSpot("F1-B1"))
    floor_1.add_spot(ElectricSpot("F1-E1"))
    parking_lot.add_floor(floor_1)
    rate = ParkingRate()
    fee_calculator = FeeCalculator(rate)
    entry_panel = EntryPanel("Entry-1")
    exit_panel = ExitPanel("Exit-1", fee_calculator)
    customer_info_portal = CustomerInfoPortal("CustomerInfo-1", fee_calculator)
    parking_lot.add_entry_panel(entry_panel)
    parking_lot.add_exit_panel(exit_panel)

    return parking_lot, rate, entry_panel, exit_panel, customer_info_portal

def menu():
    print("Welcome to the Parking Lot System!!")
    print("1. Admin: Manage Floors (Add/Remove/Modify)")
    print("2. Admin: Update Rates")
    print("3. Admin: Manage Spots (Add/Remove/Modify)")
    print("4. Admin: Add/Remove Attendant")
    print("5. Customer/Attendant: Vehicle Arrives")
    print("6. Customer: Pay at Info Portal")
    print("7. Customer/Attendant: Vehicle Exits")
    print("8. System: Show Display Board")
    print("9. Exit")
    print("-" * 20)

def main():
    parking_lot, rate, entry_panel, exit_panel, customer_info_portal = initialize_parking_lot()
    admin = Admin("Vedansh")

    parking_attendant = ParkingAttendant("Krish")
    admin.add_attendant(parking_attendant)

    active_ticket = {}

    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Enter 1.Add Floor; 2.Remove Floor; 3.Modify Floor")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                floor_number = input("Enter floor number: ")
                floor = ParkingFloor(floor_number)
                floor.add_spot(CompactSpot(f"{floor_number}-C1"))
                floor.add_spot(CompactSpot(f"{floor_number}-C2"))
                floor.add_spot(LargeSpot(f"{floor_number}-L1"))
                admin.add_parking_floor(floor)
                print(f"Floor {floor_number} added successfully.")
            elif sub_choice == "2":
                floor_number = input("Enter floor number: ")
                admin.remove_parking_floor(floor_number)
            elif sub_choice == "3":
                old_floor_number = input("Enter old floor number: ")
                new_floor_number = input("Enter new floor number: ")
                admin.modify_parking_floor(old_floor_number, new_floor_number)

        elif choice == "2":
            try:
                new_hour_1 = float(input("Enter new parking rate for hour 1: "))
                new_hour_2_3 = float(input("Enter new parking rate for hour 2 and 3: "))
                new_hour_remaining = float(input("Enter new parking rate for hour remaining: "))
                admin.update_parking_rate(rate, new_hour_1, new_hour_2_3, new_hour_remaining)
            except ValueError:
                print("Please enter a numeric value.")

        elif choice == "3":
            print("Enter 1.Add Spot; 2.Remove Spot; 3.Modify Spot")
            sub_choice = input("Enter your choice: ")
            floor_number = input("Enter floor number: ")
            if sub_choice == "1":
                spot_number = input("Enter spot number: ")
                spot_type = input("Enter spot type (1:Compact, 2:Large, 3:Motorcycle, 4:Electric, 5:Handicapped): ")
                spot = None
                if spot_type == "1": spot = CompactSpot(spot_number)
                elif spot_type == "2": spot = LargeSpot(spot_number)
                elif spot_type == "3": spot = Bike(spot_number)
                elif spot_type == "4": spot = ElectricSpot(spot_number)
                elif spot_type == "5": spot = HandicappedSpot(spot_number)
                if spot:
                    admin.add_parking_spot(floor_number, spot)
                else:
                    print("Please enter a valid spot type.")
            elif sub_choice == "2":
                spot_number = input("Enter spot number: ")
                admin.remove_parking_spot(floor_number, spot_number)
            elif sub_choice == "3":
                old_spot_number = input("Enter old spot number: ")
                new_spot_number = input("Enter new spot number: ")
                spot_type = input("New Spot Type (1:Compact, 2:Large, 3:Motorcycle, 4:Electric, 5:Handicapped):")
                spot = None
                if spot_type == "1": spot = CompactSpot(new_spot_number)
                elif spot_type == "2": spot = LargeSpot(new_spot_number)
                elif spot_type == "3": spot = Bike(new_spot_number)
                elif spot_type == "4": spot = ElectricSpot(new_spot_number)
                elif spot_type == "5": spot = HandicappedSpot(new_spot_number)
                if spot:
                    admin.modify_parking_spot(floor_number, old_spot_number, spot)
                else:
                    print("Please enter a valid spot type.")

        elif choice == "4":
            sub_choice = input("1: Add Attendant, 2: Remove Attendant: ")
            if sub_choice == "1":
                attendant_name = input("Enter parking attendant's name: ")
                parking_attendant = ParkingAttendant(attendant_name)
                admin.add_attendant(parking_attendant)
            elif sub_choice == "2":
                attendant_name = input("Enter parking attendant's name: ")

                admin.remove_attendant(attendant_name)

        elif choice == "5":
            registration_number = input("Enter registration number: ")
            vehicle_type = input("Enter Vehicle Type (1:Car, 2:Truck, 3:Motorcycle, 4:Electric, 5:Van): ")
            # vehicle = None
            if vehicle_type == "1": vehicle = Car(registration_number)
            elif vehicle_type == "2": vehicle = Truck(registration_number)
            elif vehicle_type == "3": vehicle = Bike(registration_number)
            elif vehicle_type == "4": vehicle = Electric(registration_number)
            elif vehicle_type == "5": vehicle = Van(registration_number)
            else:
                print("Please enter a valid vehicle type.")
                continue
            ticket = entry_panel.process_entry(vehicle)
            if ticket:
                active_ticket[ticket.ticket_id] = ticket

        elif choice == "6":
            ticket_id = input("Enter ticket ID: ")
            if ticket_id in active_ticket:
                ticket = active_ticket[ticket_id]
                print("Simulating duration: adding 2.5 hours to entry time...")
                ticket.entry_time = ticket.entry_time - datetime.timedelta(hours=2, minutes=30)
                payment_strategy = CreditCard()
                customer_info_portal.process_payment(ticket, payment_strategy)
            else:
                print("Please enter a valid ticket ID.")

        elif choice == "7":
            ticket_id = input("Enter ticket ID: ")
            if ticket_id in active_ticket:
                ticket = active_ticket[ticket_id]
                if ticket.status.name == "Active":
                    print("Simulating duration: adding 3.5 hours to entry time...")
                    ticket.entry_time = ticket.entry_time - datetime.timedelta(hours=3, minutes=30)
                    pay_method = input("Payment method (1: Cash, 2: Credit Card, 3: Skip if already paid): ")
                    strategy = None
                    if pay_method == "1":
                        strategy = Cash()
                    elif pay_method == "2":
                        strategy = CreditCard()

                    success = exit_panel.process_exit(ticket, strategy)
                    if success:
                        del active_ticket[ticket_id]
                else:
                    print("Ticket not found.")

        elif choice == "8":
            print("----------Display Board----------")
            for floor in parking_lot.floors.values():
                print(f"Floor {floor.floor_number}:")
                floor.display_board.show_board(parking_lot.is_full())

        elif choice == "9":
            print("Exiting...")
            break

        else:
            print("Please enter a valid choice.")

if __name__ == "__main__":
    main()