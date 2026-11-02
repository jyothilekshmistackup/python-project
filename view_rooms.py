# Display all rooms or only available rooms.

from database import load_data

def view_rooms(available_only=False):
    data = load_data()

    print("\n--- ROOM LIST ---")
    if len(data["rooms"]) == 0:
        print("No rooms have been added.")
        return

    for room in data["rooms"]:
        is_booked = False

        # Check whether this room has a current booking.
        for booking in data["bookings"]:
            if booking["room_no"] == room["room_no"] and booking["status"] == "confirmed":
                is_booked = True

        if available_only and is_booked:
            continue

        if is_booked:
            status = "Booked"
        else:
            status = "Available"

        print("-------------------------")
        print("Room number:", room["room_no"])
        print("Room type:", room["room_type"])
        print("Price per night:", room["price"])
        print("Guest capacity:", room["capacity"])
        print("Status:", status)
