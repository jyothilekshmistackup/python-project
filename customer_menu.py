
from view_rooms import view_rooms
from search_room import search_room
from book_room import book_room
from view_bookings import view_bookings
from cancel_booking import cancel_booking
from logout import logout

def customer_menu(username):
    while True:
        print("\n========== CUSTOMER MENU ==========")
        print("1. View available rooms")
        print("2. Search room")
        print("3. Book room")
        print("4. View my bookings")
        print("5. Cancel booking")
        print("6. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            view_rooms(available_only=True)
        elif choice == "2":
            search_room()
        elif choice == "3":
            book_room(username)
        elif choice == "4":
            view_bookings(username)
        elif choice == "5":
            cancel_booking(username)
        elif choice == "6":
            logout()
            break
        else:
            print("Invalid option.")
