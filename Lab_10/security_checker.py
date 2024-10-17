import json
 
def save_user_data(username, password):
    # Load existing user data from the JSON file
    try:
        with open("user_data.json", "r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}
 
    # Add new user data
    existing_data[username] = password
 
    # Save the updated user data to the JSON file
    with open("user_data.json", "w") as file:
        json.dump(existing_data, file)
 
def create_new_user():
    while True:
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
 
        try:
            # Validate the password
            if len(password) < 8 or password.startswith(' ') or password.endswith(' ') or password[0].isdigit():
                raise ValueError("Invalid password. Please follow the password rules.")
           
            # Confirm the password
            confirm_password = input("Re-enter the password to confirm: ")
            if password != confirm_password:
                raise ValueError("Passwords do not match. Please try again.")
 
            # Save the user data
            save_user_data(username, password)
            print("New user created successfully!\n")
            break
 
        except ValueError as e:
            print(f"Error: {e}")
 
def login_existing_user():
    attempts = 3
 
    while attempts > 0:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
 
        # Load user data from the JSON file
        try:
            with open("user_data.json", "r") as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = {}
 
        # Check if the entered username exists and the password is correct
        if username in user_data and user_data[username] == password:
            print("Welcome, {}!".format(username))
            break
        else:
            attempts -= 1
            print(f"Invalid username or password. {attempts} attempts remaining.\n")
 
    if attempts == 0:
        print("You are locked out. Please contact support.")
 
def main():
    while True:
        print("\n1. New user")
        print("2. Existing user")
        print("3. Exit")
 
        choice = input("Enter your choice (1, 2, or 3): ")
 
        if choice == "1":
            create_new_user()
        elif choice == "2":
            login_existing_user()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
 
if __name__ == "__main__":
    main()