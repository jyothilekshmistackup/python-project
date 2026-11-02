
from database import load_data, save_data

def delete_room():
    data = load_data()

    try:
        room_no = int(input("Enter room number to delete: "))
    except ValueError:
        print("Enter a valid room number.")
        return

    for booking in data["bookings"]:
        if booking["room_no"] == room_no and booking["status"] == "confirmed":
            print("This room has an active booking. Cancel the booking first.")
            return

    for room in data["rooms"]:
        if room["room_no"] == room_no:
            data["rooms"].remove(room)
            save_data(data)
            print("Room deleted successfully.")
            return

    print("Room not found.")
