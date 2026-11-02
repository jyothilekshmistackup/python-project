# Login checks the username and password.

from database import load_data

def login():
    data = load_data()

    print("\n--- LOGIN ---")
    username = input("Username: ").strip()
    password = input("Password: ")

    for user in data["users"]:
        if user["username"] == username and user["password"] == password:
            print("Login successful.")
            return user

    print("Incorrect username or password.")
    return None
