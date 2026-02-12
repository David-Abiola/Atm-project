# ATM PROJECT
import time
from datetime import datetime
# CREATE ACCOUNT
def create():
    try:
        print("\nWelcome to the create account session")

        while True:
            name = input("Enter your name: ").strip()
            if name.isalpha():
                break
            else:
                print("Invalid name. Use letters only.")
        while True:
            email = input("enter your email ")
            if "@gmail.com" not in email:
                print("Invalid email. format(name@gmail.com).")
                email = input("enter email ")
            else:
                print("authenticating email")
                time.sleep(5)
                print("email accepted")
            print("\nDate of birth")

            day = int(input("Enter day only: "))
            while day > 31 or day < 1:
                day = int(input("Invalid day. Enter again: "))

            month = int(input("Enter month only: "))
            while month > 12 or month < 1:
                month = int(input("Invalid month. Enter again: "))

            year = int(input("Enter year only: "))
            # age = 2026 - year

            if year >= 2008:
                print("You are under 18, account denied.")
                return

            print("\nLet's proceed")

            while True:
                password = input("Enter your password: ").strip()
                confirm = input("confirm password ")
                if password == confirm:
                    print("password accepted")
                else:
                    print("password no equivalent to confirm")
                    password = input("Enter your password: ").strip()
                    confirm = input("confirm password ")
                if len(password) >= 4:
                    break
                else:
                    print("Password must be more than 4 or more than 4 characters")

            balance = 0
            #code to open and store file into app.txt
            with open("app.txt", "a") as file:
                file.write(name.lower() + "," + email.lower() + "," +  password + "," + str(balance) + "\n")

            print("\nAccount created successfully")
            break

    except ValueError:
        print("Wrong value entered.")


# LOAD USERS
def load_users():
    users = {}

    try:
        with open("app.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                name, password, email, balance = line.split(",")
                users[name] = {"password": password, "email": email, "balance": int(balance)}
    except FileNotFoundError:
        pass

    return users


# SAVE USERS
def save_users(users):
    with open("app.txt", "w") as file:
        for name in users:
            password = users[name]["password"]
            balance = users[name]["balance"]
            email = users[name]["email"]
            file.write(name + "," + email + "," + password + "," + str(balance) + "\n")


# LOGIN MENU
def atm_menu(username, users):
    while True:
        print("\nATM MENU")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Logout")

        choice = input("Enter: ")

        if choice == "1":
            print("Your balance is:", users[username]["balance"])

        elif choice == "2":
            try:
                amount = int(input("Enter amount to deposit: "))
                if amount > 0:
                    users[username]["balance"] += amount
                    save_users(users)
                    print(f"Deposit successful at {datetime.now()}")
                else:
                    print("Invalid amount")
            except ValueError:
                print("Enter numbers only")

        elif choice == "3":
            try:
                amount = int(input("Enter amount to withdraw: "))
                if amount > users[username]["balance"]:
                    print("Insufficient balance")
                elif amount <= 0:
                    print("Invalid amount")
                else:
                    users[username]["balance"] -= amount
                    save_users(users)
                    print(f"Withdrawal successful at {datetime.now()}")
            except ValueError:
                print("Enter numbers only")

        elif choice == "4":
            receiver = input("Enter receiver name: ").strip().lower()

            if receiver not in users:
                print("Receiver not found")
                continue

            try:
                amount = int(input("Enter amount to transfer: "))
                message = input("add message ")

                if amount <= 0:
                    print("Invalid amount")
                elif amount > users[username]["balance"]:
                    print("Insufficient balance")
                else:
                    users[username]["balance"] -= amount
                    users[receiver]["balance"] += amount
                    save_users(users)
                    time.sleep(5)
                    print(f"Transfer successful to {receiver} at {datetime.now()}", )
            except ValueError:
                print("Enter numbers only")

        elif choice == "5":
            print("Logged out")
            break

        else:
            print("Invalid option")


# LOGIN SESSION
def login():
    print("\nWelcome to the login session")

    users = load_users()
    attempts = 3

    while attempts > 0:
        name = input("Enter your name: ").strip().lower()
        password = input("Enter your password: ").strip()

        if password in users and users[name]["password"] and users[name]["email"] == name:
            print("Login successful")
            atm_menu(name, users)
            return
        else:
            attempts -= 1
            print("Wrong login details")
            print("Attempts left:", attempts)

    print("Too many failed attempts")


# ===== MAIN MENU =====
print("Welcome to our ATM machine")
print("Enter 1 to create account")
print("Enter 2 to login")
print("quit to exit")

user_input = input("Enter: ")

if user_input == "quit":
    print("ok")

elif user_input == "1":
    create()

elif user_input == "2":
    login()

else:
    print("Option not available.")
