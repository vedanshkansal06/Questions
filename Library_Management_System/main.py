from datetime import date, timedelta
from States import ReservationStatus
from models.Rack import Rack
from models.Library_Card import LibraryCard
from models.Person import Person, Member, Librarian
from search.Catalog import Catalog
from search.Book_Search_Criteria import BookSearchCriteria
from notifications.Notification import SMSNotification
from notifications.Notification_Services import NotificationService
from core.Library import Library


def initial_data(library: Library):
    card1 = LibraryCard("M0001", date.today())
    lib = Librarian("Vedansh", "1234", card1, "L0001")
    library.add_librarian(lib)

    mem1_card = LibraryCard("M0002", date.today())
    mem1 = Member("Aman", "2345", mem1_card)
    lib.add_member(mem1)

    mem2_card = LibraryCard("M0003", date.today())
    mem2 = Member("Harsh", "9876", mem2_card)
    lib.add_member(mem2)

    mem3_card = LibraryCard("M0004", date.today())
    mem3 = Member("Krish", "5555", mem3_card)
    lib.add_member(mem3)

    lib.add_book(1, "Lord of the Rings", "Fantasy", "1974", ["J. R. R. Tolkien"])
    lib.add_book(2, "Harry Potter", "Fantasy", "1997", ["J. K. Rowling"])
    lib.add_book(3, "The Great Gatsby", "Fiction", "1925", ["F. Scott Fitzgerald"])
    lib.add_book(4, "Clean Code", "Technology", "2008", ["Robert C. Martin"])

    lib.add_book_item(1, "B0001", Rack(1, "A1"))
    lib.add_book_item(1, "B0002", Rack(1, "A2"))
    lib.add_book_item(2, "B0003", Rack(2, "B1"))
    lib.add_book_item(3, "B0004", Rack(3, "C1"))
    lib.add_book_item(4, "B0005", Rack(4, "D1"))
    lib.add_book_item(4, "B0006", Rack(4, "D2"))

    mem1.checkout_book("B0001", date.today())
    mem1.checkout_book("B0003", date.today())
    mem2.reserve_book(1, date.today())
    mem3.reserve_book(2, date.today())

    past_date = date.today() - timedelta(days=20)

    mem3.checkout_book("B0005", past_date)
    mem3.return_book("B0005", date.today())

def member_menu(member: Person):
    while True:
        print("\n----- MEMBER MENU -----")
        print("1. Reserve Book")
        print("2. Check Out Book")
        print("3. Renew Book")
        print("4. Return Book")
        print("5. Account Status")
        print("6. Pay Fine")
        print("7. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            isbn = int(input("Enter book ISBN to reserve: "))
            try:
                reservation = member.reserve_book(isbn, date.today())
                print(f"Reservation Status: {reservation.status}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            book_barcode = input("Enter book barcode: ")
            try:
                lending = member.checkout_book(book_barcode, date.today())
                print(f"Book Successfully Checked Out, Due Date: {lending.due_date}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            book_barcode = input("Enter book barcode: ")
            try:
                member.renew_book(book_barcode, date.today())
                print("Book renewed successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            book_barcode = input("Enter book barcode: ")
            try:
                member.return_book(book_barcode, date.today())
                print("Book returned successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            print(f"Status: {member.state.name}")
            print(f"Fine Balance: {member.account.fine_balance}")
            print("Active Lendings:")
            for lending in member.account.active_lendings:
                print(f"{lending.book_item.book} - {lending.book_item.barcode}, Due Date: {lending.due_date}")
            print("Active Reservations:")
            for reservation in member.account.reservations:
                print(f"{reservation.book.title}, Status: {reservation.status.name}")

        elif choice == "6":
            amount = float(input("Enter amount to pay (in dollars): "))
            member.account.pay_fine(amount)
            print(f"Remaining Fine: {member.account.fine_balance}")

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please try again.")

def librarian_menu(librarian: Librarian):
    while True:
        print("\n----- LIBRARIAN MENU -----")
        print("1. Enter Member Menu")
        print("2. Add Book")
        print("3. Edit Book")
        print("4. Delete Book")
        print("5. Add Book Item")
        print("6. Edit Book Item")
        print("7. Delete Book Item")
        print("8. Add Member")
        print("9. Remove Member")
        print("10. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            member_menu(librarian)

        elif choice == "2":
            isbn = int(input("Enter book ISBN: "))
            title = input("Enter book title: ")
            subject = input("Enter book subject: ")
            publication_date = input("Enter book publication date: ")
            print("Enter Author Names (Enter '0' to stop):")
            author_names = []
            i = 1
            while True:
                user_input = input(f"{i}. ")
                if user_input == "0":
                    break
                author_names.append(user_input)
                i += 1
            librarian.add_book(isbn, title, subject, publication_date, author_names)
            print("Book added successfully.")

        elif choice == "3":
            try:
                isbn = int(input("Enter book ISBN: "))
                title = input("Enter book title: ")
                subject = input("Enter book subject: ")
                publication_date = input("Enter book publication date: ")
                librarian.edit_book(isbn, title, subject, publication_date)
                print("Book edited successfully.")
            except ValueError:
                print("Invalid ISBN.")

        elif choice == "4":
            try:
                isbn = int(input("Enter book ISBN: "))
                librarian.remove_book(isbn)
                print("Book removed successfully.")
            except ValueError:
                print("Invalid ISBN.")

        elif choice == "5":
            try:
                isbn = int(input("Enter book ISBN: "))
                barcode = input("Enter book barcode: ")
                rack_num = int(input("Enter rack number: "))
                rack_identifier = input("Enter rack location: ")
                rack = Rack(rack_num, rack_identifier)
                librarian.add_book_item(isbn, barcode, rack)
                print("Book Item added successfully.")
            except ValueError:
                print("Invalid Inputs.")

        elif choice == "6":
            try:
                isbn = int(input("Enter book ISBN: "))
                barcode = input("Enter book barcode: ")
                rack_num = int(input("Enter rack number: "))
                rack_identifier = input("Enter rack location: ")
                rack = Rack(rack_num, rack_identifier)
                librarian.edit_book_item(isbn, barcode, rack)
                print("Book Item edited successfully.")
            except ValueError:
                print("Invalid Inputs.")

        elif choice == "7":
            try:
                isbn = int(input("Enter book ISBN: "))
                barcode = input("Enter book barcode: ")
                librarian.remove_book_item(isbn, barcode)
                print("Book Item removed successfully.")
            except ValueError:
                print("Invalid Inputs.")

        elif choice == "8":
            try:
                barcode = input("Enter barcode: ")
                card = LibraryCard(barcode, date.today())
                name = input("Enter member name: ")
                phone = input("Enter phone number: ")
                member = Member(name, phone, card)
                librarian.add_member(member)
                print("Member added successfully.")
            except ValueError:
                print("Invalid Inputs.")

        elif choice == "9":
            try:
                barcode = input("Enter barcode: ")
                librarian.cancel_member(barcode)
                print("Member canceled successfully.")
            except ValueError:
                print("Invalid Inputs.")

        elif choice == "10":
            break

        else:
            print("Invalid Input.")


def main():
    catalog = Catalog()
    sms_notification = SMSNotification()
    notification_service = NotificationService(sms_notification)
    library = Library(catalog, notification_service)
    initial_data(library)

    while True:
        print("Welcome to Library Management System!")
        print("1. Enter Librarian Menu")
        print("2. Enter Member Menu")
        print("3. Search Books")
        print("4. Trigger System")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = input("Enter employee ID: ")
            librarian = library.get_librarian(emp_id)
            if librarian:
                librarian_menu(librarian)
            else:
                print("Librarian not found.")

        elif choice == "2":
            barcode = input("Enter barcode: ")
            member = library.get_member(barcode)
            if member:
                member_menu(member)
            else:
                print("Member not found.")

        elif choice == "3":
            try:
                title = input("Enter title: ")
                author = input("Enter author: ")
                publication_date = input("Enter publication date: ")
                criteria = BookSearchCriteria(title, author, publication_date)
                result = library.catalog.search_book(criteria)
                for book in result:
                    available = len(book.get_available_books())
                    print(f"Title: {book.title}, ISBN: {book.ISBN}, Available Copies: {available}")
                    for item in book.book_items:
                        print(f"Barcode: {item.barcode}, Status: {item.status}")
            except ValueError:
                print("Invalid Inputs.")

        elif choice == "4":
            days = input("Enter number of days for overdue notifications: ")
            future_date = date.today() + timedelta(days=int(days))
            library.notification_service.check_over_due_loan(future_date)
            if not library.notification_service.check_over_due_loan(future_date):
                print("No books are overdue.")

        elif choice == "5":
            break

        else:
            print("Invalid Inputs.")

if __name__ == "__main__":
    main()

