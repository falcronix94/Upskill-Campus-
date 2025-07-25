import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# Initialize the file if it doesn't exist
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount", "Description"])

# Add a transaction
def add_transaction():
    t_type = input("Enter type (Income/Expense): ").capitalize()
    category = input("Enter category (Food, Travel, Salary, etc.): ")
    amount = float(input("Enter amount: ₹"))
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, t_type, category, amount, description])
    print("Transaction recorded successfully.")

# View all transactions
def view_transactions():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))

# Summary report
def show_summary():
    total_income = 0
    total_expense = 0

    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row["Amount"])
            if row["Type"] == "Income":
                total_income += amount
            elif row["Type"] == "Expense":
                total_expense += amount

    print("\n=== Financial Summary ===")
    print(f"Total Income: ₹{total_income}")
    print(f"Total Expenses: ₹{total_expense}")
    print(f"Balance: ₹{total_income - total_expense}")

# Menu
def menu():
    init_file()
    while True:
        print("\n=== Expense Tracker Menu ===")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            show_summary()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please try