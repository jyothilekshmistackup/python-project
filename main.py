
from database import create_database
from signup import signup
from login import login
from admin_menu import admin_menu
from customer_menu import customer_menu

def main():
    create_database()

    while True:
        print("\n========== HOTEL MANAGEMENT SYSTEM ==========")
        print("1. Sign up")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            signup()

        elif choice == "2":
            user = login()

            if user is not None:
                if user["role"] == "admin":
                    admin_menu()
                else:
                    customer_menu(user["username"])

        elif choice == "3":
            print("Thank you for using the Hotel Management System.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
