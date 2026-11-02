# A customer can cancel their own booking.

from database import load_data, save_data

def cancel_booking(username):
    data = load_data()

    try:
        booking_id = int(input("Enter booking ID to cancel: "))
    except ValueError:
        print("Enter a valid booking ID.")
        return

    for booking in data["bookings"]:
        if (booking["booking_id"] == booking_id
                and booking["username"] == username
                and booking["status"] == "confirmed"):
            booking["status"] = "cancelled"
            save_data(data)
            print("Booking cancelled successfully.")
            return

    print("Active booking not found.")
