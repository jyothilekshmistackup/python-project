# Menu for the administrator.

from add_room import add_room
from view_rooms import view_rooms
from search_room import search_room
from delete_room import delete_room
from view_bookings import view_bookings
from logout import logout

def admin_menu():
    while True:
        print("\n========== ADMIN MENU ==========")
        print("1. Add room")
        print("2. View rooms")
        print("3. Search room")
        print("4. Delete room")
        print("5. View all bookings")
        print("6. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            add_room()
        elif choice == "2":
            view_rooms()
        elif choice == "3":
            search_room()
        elif choice == "4":
            delete_room()
        elif choice == "5":
            view_bookings()
        elif choice == "6":
            logout()
            break
        else:
            print("Invalid option.")
