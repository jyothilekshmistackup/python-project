# Search for a room using its room number.

from database import load_data

def search_room():
    data = load_data()

    try:
        room_no = int(input("Enter room number to search: "))
    except ValueError:
        print("Enter a valid room number.")
        return

    for room in data["rooms"]:
        if room["room_no"] == room_no:
            print("\nRoom found.")
            print("Room number:", room["room_no"])
            print("Room type:", room["room_type"])
            print("Price per night:", room["price"])
            print("Guest capacity:", room["capacity"])
            return

    print("Room not found.")
