# Display bookings for one customer or all bookings for admin.

from database import load_data

def view_bookings(username=None):
    data = load_data()
    found = False

    print("\n--- BOOKINGS ---")
    for booking in data["bookings"]:
        if username is None or booking["username"] == username:
            found = True
            print("-------------------------")
            print("Booking ID:", booking["booking_id"])
            print("Customer:", booking["username"])
            print("Room number:", booking["room_no"])
            print("Check-in:", booking["check_in"])
            print("Check-out:", booking["check_out"])
            print("Guests:", booking["guests"])
            print("Total price:", booking["total_price"])
            print("Status:", booking["status"])

    if not found:
        print("No bookings found.")
