# This file contains functions for reading and writing the JSON file.

import json
import os

FILE_NAME = "database.json"

def create_database():
    # Create the JSON file the first time the program runs.
    if not os.path.exists(FILE_NAME):
        data = {
            "users": [
                {"username": "admin", "password": "admin123", "role": "admin"}
            ],
            "rooms": [],
            "bookings": [],
            "next_booking_id": 1
        }
        save_data(data)
        print("Database created.")
        print("Default admin login: admin / admin123")

def load_data():
    # Read all information from the JSON file.
    with open(FILE_NAME, "r") as file:
        data = json.load(file)
    return data

def save_data(data):
    # Save all information into the JSON file.
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
