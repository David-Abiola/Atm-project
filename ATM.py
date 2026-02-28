from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

FILE_NAME = "app.txt"


# =========================
# LOAD USERS
# =========================
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


# =========================
# SAVE USERS
# =========================
def save_users(users):
    with open(FILE_NAME, "w") as file:
        for name, data in users.items():
            file.write(f"{name},{data['email']},{data['password']},{data['balance']}\n")


# =========================
# CREATE ACCOUNT
# =========================
@app.route("/create", methods=["POST"])
def create_account():
    data = request.json
    users = load_users()

    name = data.get("name", "").strip().lower()
    email = data.get("email", "").strip().lower()
    password = data.get("password", "").strip()
    year = int(data.get("year", 0))

    if not name.isalpha():
        return jsonify({"error": "Invalid name"}), 400

    if not email.endswith("@gmail.com"):
        return jsonify({"error": "Invalid email"}), 400

    if year >= 2008:
        return jsonify({"error": "Under 18"}), 403

    if len(password) < 4:
        return jsonify({"error": "Password too short"}), 400

    if name in users:
        return jsonify({"error": "User already exists"}), 400

    users[name] = {
        "email": email,
        "password": password,
        "balance": 0
    }

    save_users(users)

    return jsonify({"message": "Account created successfully"}), 201


# =========================
# LOGIN
# =========================
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    users = load_users()

    name = data.get("name", "").strip().lower()
    password = data.get("password", "").strip()

    if name in users and users[name]["password"] == password:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"error": "Invalid credentials"}), 401


# =========================
# CHECK BALANCE
# =========================
@app.route("/balance/<username>", methods=["GET"])
def check_balance(username):
    users = load_users()

    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "balance": users[username]["balance"]
    })


# =========================
# DEPOSIT
# =========================
@app.route("/deposit", methods=["POST"])
def deposit():
    data = request.json
    users = load_users()

    name = data.get("name")
    amount = int(data.get("amount", 0))

    if name not in users:
        return jsonify({"error": "User not found"}), 404

    if amount <= 0:
        return jsonify({"error": "Invalid amount"}), 400

    users[name]["balance"] += amount
    save_users(users)

    return jsonify({
        "message": "Deposit successful",
        "balance": users[name]["balance"],
        "time": str(datetime.now())
    })


# =========================
# WITHDRAW
# =========================
@app.route("/withdraw", methods=["POST"])
def withdraw():
    data = request.json
    users = load_users()

    name = data.get("name")
    amount = int(data.get("amount", 0))

    if name not in users:
        return jsonify({"error": "User not found"}), 404

    if amount <= 0:
        return jsonify({"error": "Invalid amount"}), 400

    if amount > users[name]["balance"]:
        return jsonify({"error": "Insufficient funds"}), 400

    users[name]["balance"] -= amount
    save_users(users)

    return jsonify({
        "message": "Withdrawal successful",
        "balance": users[name]["balance"],
        "time": str(datetime.now())
    })


# =========================
# TRANSFER
# =========================
@app.route("/transfer", methods=["POST"])
def transfer():
    data = request.json
    users = load_users()

    sender = data.get("sender")
    receiver = data.get("receiver")
    amount = int(data.get("amount", 0))

    if sender not in users or receiver not in users:
        return jsonify({"error": "User not found"}), 404

    if amount <= 0:
        return jsonify({"error": "Invalid amount"}), 400

    if amount > users[sender]["balance"]:
        return jsonify({"error": "Insufficient balance"}), 400

    users[sender]["balance"] -= amount
    users[receiver]["balance"] += amount
    save_users(users)

    return jsonify({
        "message": "Transfer successful",
        "time": str(datetime.now())
    })


# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True)