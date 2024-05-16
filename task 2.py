
import json
import os

def load_data():
    if os.path.exists("budget_data.json"):
        with open("budget_data.json", "r") as file:
            return json.load(file)
    else:
        return {"expenses": [], "income": []}

def save_data(data):
    with open("budget_data.json", "w") as file:
        json.dump(data, file)

def add_expense(data):
    category = input("Enter expense category: ")
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    data["expenses"].append({"category": category, "description": description, "amount": amount})
    print("Expense added successfully.")

def add_income(data):
    category = input("Enter income category: ")
    description = input("Enter income description: ")
    amount = float(input("Enter income amount: "))
    data["income"].append({"category": category, "description": description, "amount": amount})
    print("Income added successfully.")

def calculate_budget(data):
    total_income = sum(income["amount"] for income in data["income"])
    total_expenses = sum(expense["amount"] for expense in data["expenses"])
    remaining_budget = total_income - total_expenses
    print(f"Remaining Budget: ${remaining_budget}")

def analyze_expenses(data):
    expense_categories = {}
    for expense in data["expenses"]:
        category = expense["category"]
        amount = expense["amount"]
        if category in expense_categories:
            expense_categories[category] += amount
        else:
            expense_categories[category] = amount
    print("Expense Analysis:")
    for category, amount in expense_categories.items():
        print(f"{category}: ${amount}")

def main():
    data = load_data()
    while True:
        print("\n1. Add Expense")
        print("2. Add Income")
        print("3. Calculate Budget")
        print("4. Analyze Expenses")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense(data)
        elif choice == "2":
            add_income(data)
        elif choice == "3":
            calculate_budget(data)
        elif choice == "4":
            analyze_expenses(data)
        elif choice == "5":
            save_data(data)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
