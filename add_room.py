# Admin can add a new room.

from database import load_data, save_data

def add_room():
    data = load_data()

    print("\n--- ADD ROOM ---")
    try:
        room_no = int(input("Room number: "))
        price = float(input("Price per night: "))
        capacity = int(input("Maximum number of guests: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    for room in data["rooms"]:
        if room["room_no"] == room_no:
            print("This room number already exists.")
            return

    room_type = input("Room type (Single/Double/Deluxe): ").strip()

    if room_type == "":
        print("Room type cannot be empty.")
        return

    new_room = {
        "room_no": room_no,
        "room_type": room_type,
        "price": price,
        "capacity": capacity
    }

    data["rooms"].append(new_room)
    save_data(data)
    print("Room added successfully.")
