# Customer can book an available room.

from datetime import datetime
from database import load_data, save_data

def book_room(username):
    data = load_data()

    print("\n--- BOOK ROOM ---")
    try:
        room_no = int(input("Room number: "))
        guests = int(input("Number of guests: "))
    except ValueError:
        print("Enter valid numbers.")
        return

    selected_room = None
    for room in data["rooms"]:
        if room["room_no"] == room_no:
            selected_room = room

    if selected_room is None:
        print("Room not found.")
        return

    if guests < 1 or guests > selected_room["capacity"]:
        print("Guest count is outside this room's capacity.")
        return

    check_in_text = input("Check-in date (YYYY-MM-DD): ")
    check_out_text = input("Check-out date (YYYY-MM-DD): ")

    try:
        check_in = datetime.strptime(check_in_text, "%Y-%m-%d").date()
        check_out = datetime.strptime(check_out_text, "%Y-%m-%d").date()
    except ValueError:
        print("Please enter dates in YYYY-MM-DD format.")
        return

    if check_in < datetime.today().date() or check_out <= check_in:
        print("Invalid dates. Check-out must be after check-in.")
        return

    # Check whether the room is already booked for these dates.
    for booking in data["bookings"]:
        if booking["room_no"] == room_no and booking["status"] == "confirmed":
            old_in = datetime.strptime(booking["check_in"], "%Y-%m-%d").date()
            old_out = datetime.strptime(booking["check_out"], "%Y-%m-%d").date()

            if check_in < old_out and old_in < check_out:
                print("This room is already booked for those dates.")
                return

    nights = (check_out - check_in).days
    total_price = nights * selected_room["price"]

    booking = {
        "booking_id": data["next_booking_id"],
        "username": username,
        "room_no": room_no,
        "check_in": check_in_text,
        "check_out": check_out_text,
        "guests": guests,
        "nights": nights,
        "total_price": total_price,
        "status": "confirmed"
    }

    data["bookings"].append(booking)
    data["next_booking_id"] = data["next_booking_id"] + 1
    save_data(data)

    print("Room booked successfully.")
    print("Your booking ID is:", booking["booking_id"])
    print("Number of nights:", nights)
    print("Total price:", total_price)
