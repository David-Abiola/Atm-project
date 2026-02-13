# ===== ATM PROJECT =====
import time
from datetime import datetime


FILE_NAME = "app.txt"


# ---------- CREATE ACCOUNT ----------
def create_account():
    print("\n=== CREATE ACCOUNT ===")

    # NAME
    while True:
        name = input("Enter your name: ").strip().lower()
        if name.isalpha():
            break
        print("Invalid name. Use letters only.")

    # EMAIL LOOP
    while True:
        email = input("Enter your email: ").strip().lower()
        if email.endswith("@gmail.com") and "@" in email:
            print("Authenticating email...")
            time.sleep(2)
            print("Email accepted")
            break
        print("Invalid email format (example: name@gmail.com)")

    # DATE OF BIRTH
    print("\nDate of Birth")

    while True:
        try:
            day = int(input("Day (1-31): "))
            if 1 <= day <= 31:
                break
        except ValueError:
            pass
        print("Invalid day")

    while True:
        try:
            month = int(input("Month (1-12): "))
            if 1 <= month <= 12:
                break
        except ValueError:
            pass
        print("Invalid month")

    while True:
        try:
            year = int(input("Year: "))
            break
        except ValueError:
            print("Enter numbers only")

    if year >= 2008:
        print("You are under 18. Account denied.")
        return

    # PASSWORD CONFIRM LOOP
    while True:
        password = input("Enter password (min 4 chars): ").strip()
        confirm = input("Confirm password: ").strip()

        if len(password) < 4:
            print("Password too short")
            continue

        if password != confirm:
            print("Passwords do not match")
            continue

        print("Password accepted")
        break

    balance = 0

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{email},{password},{balance}\n")

    print("Account created successfully!")


# ---------- LOAD USERS ----------
def load_users():
    users = {}

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                if line.strip() == "":
                    continue
                name, email, password, balance = line.strip().split(",")
                users[name] = {
                    "email": email,
                    "password": password,
                    "balance": int(balance)
                }
    except FileNotFoundError:
        pass

    return users


# ---------- SAVE USERS ----------
def save_users(users):
    with open(FILE_NAME, "w") as file:
        for name, data in users.items():
            file.write(f"{name},{data['email']},{data['password']},{data['balance']}\n")


# ---------- ATM MENU ----------
def atm_menu(username, users):
    while True:
        print("\n=== ATM MENU ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            print("Balance:", users[username]["balance"])

        elif choice == "2":
            try:
                amount = int(input("Deposit amount: "))
                if amount > 0:
                    users[username]["balance"] += amount
                    save_users(users)
                    print("Deposit successful", datetime.now())
                else:
                    print("Invalid amount")
            except ValueError:
                print("Numbers only")

        elif choice == "3":
            try:
                amount = int(input("Withdraw amount: "))
                if amount <= 0:
                    print("Invalid amount")
                elif amount > users[username]["balance"]:
                    print("Insufficient funds")
                else:
                    users[username]["balance"] -= amount
                    save_users(users)
                    print("Withdrawal successful", datetime.now())
            except ValueError:
                print("Numbers only")

        elif choice == "4":
            receiver = input("Receiver name: ").strip().lower()

            if receiver not in users:
                print("User not found")
                continue

            try:
                amount = int(input("Transfer amount: "))
                if amount <= 0:
                    print("Invalid amount")
                elif amount > users[username]["balance"]:
                    print("Insufficient balance")
                else:
                    users[username]["balance"] -= amount
                    users[receiver]["balance"] += amount
                    save_users(users)
                    print("Transfer successful", datetime.now())
            except ValueError:
                print("Numbers only")

        elif choice == "5":
            print("Logged out")
            break

        else:
            print("Invalid option")


# ---------- LOGIN ----------
def login():
    users = load_users()
    attempts = 3

    while attempts > 0:
        name = input("Name: ").strip().lower()
        password = input("Password: ").strip()

        if name in users and users[name]["password"] == password:
            print("Login successful!")
            atm_menu(name, users)
            return
        else:
            attempts -= 1
            print("Wrong details. Attempts left:", attempts)

    print("Too many failed attempts.")


# ---------- MAIN ----------
while True:
    print("\n=== ATM MACHINE ===")
    print("1. Create Account")
    print("2. Login")
    print("3. Quit")

    option = input("Select: ")

    if option == "1":
        create_account()
    elif option == "2":
        login()
    elif option == "3":
        print("Goodbye")
        break
    else:
        print("Invalid option")
