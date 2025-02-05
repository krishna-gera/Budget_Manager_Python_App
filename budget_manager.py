import datetime
import csv
import os

class BudgetManager:
    def __init__(self, weekly_limit):
        self.weekly_limit = weekly_limit
        self.categories = {
            '1': 'food_and_groceries',
            '2': 'transportation',
            '3': 'healthcare',
            '4': 'savings_and_emergency_fund',
            '5': 'entertainment',
            '6': 'personal_care',
            '7': 'miscellaneous'
        }
        self.expenses = {category: 0 for category in self.categories.values()}
        self.category_limits = {
            'food_and_groceries': 0.25 * self.weekly_limit,
            'transportation': 0.10 * self.weekly_limit,
            'healthcare': 0.15 * self.weekly_limit,
            'savings_and_emergency_fund': 0.20 * self.weekly_limit,
            'entertainment': 0.10 * self.weekly_limit,
            'personal_care': 0.05 * self.weekly_limit,
            'miscellaneous': 0.05 * self.weekly_limit
        }
        self.total_spent = 0
        self.start_date = datetime.datetime.now()
        self.csv_file = 'budget_passbook.csv'
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['date', 'category', 'amount'])
        self.load_data()

    def load_data(self):
        if os.path.exists(self.csv_file):
            with open(self.csv_file, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    _, category, amount = row
                    self.expenses[category] += float(amount)
                    self.total_spent += float(amount)
            print("Data loaded successfully.")

    def save_data(self, category, amount):
        with open(self.csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.datetime.now(), category, amount])

    def add_expense(self):
        print("Select a category:")
        for key, value in self.categories.items():
            print(f"{key}. {value}")
        category_key = input("Enter the category number: ")
        if category_key in self.categories:
            amount = float(input("Enter the amount: "))
            category = self.categories[category_key]
            self.expenses[category] += amount
            self.total_spent += amount
            self.save_data(category, amount)
            self.check_budget()
        else:
            print(f"Category '{category_key}' does not exist.")

    def show_expenses(self):
        print("Expenses:")
        for category, amount in self.expenses.items():
            limit_left = self.category_limits[category] - amount
            print(f"{category}: {amount}, Limit left: {limit_left}")

    def check_budget(self):
        if self.total_spent > self.weekly_limit:
            print("Alert: You have exceeded your weekly budget!")
        else:
            print(f"Total spent: {self.total_spent}. Remaining budget: {self.weekly_limit - self.total_spent}")

    def reset_weekly_budget(self):
        current_date = datetime.datetime.now()
        if (current_date - self.start_date).days >= 7:
            self.expenses = {key: 0 for key in self.expenses}
            self.total_spent = 0
            self.start_date = current_date
            print("Weekly budget has been reset.")
        else:
            print("It's not time to reset the budget yet.")

    def change_weekly_limit(self):
        new_limit = float(input("Enter the new weekly limit: "))
        self.weekly_limit = new_limit
        self.category_limits = {
            'food_and_groceries': 0.25 * self.weekly_limit,
            'transportation': 0.10 * self.weekly_limit,
            'healthcare': 0.15 * self.weekly_limit,
            'savings_and_emergency_fund': 0.20 * self.weekly_limit,
            'entertainment': 0.10 * self.weekly_limit,
            'personal_care': 0.05 * self.weekly_limit,
            'miscellaneous': 0.05 * self.weekly_limit
        }
        print(f"Weekly limit has been updated to {self.weekly_limit}")

    def set_category_limits(self):
        print("Set limits for each category:")
        for category in self.categories.values():
            limit = float(input(f"Enter the limit for {category}: "))
            self.category_limits[category] = limit
        print("Category limits have been updated.")

# Main menu
print("Welcome to the Budget Manager")
weekly_limit = float(input("Enter your weekly budget limit: "))
budget_manager = BudgetManager(weekly_limit)
if budget_manager.weekly_limit == 0:
    print("Initial alert: Weekly limit is set to 0. Please set the weekly limit first.")
    budget_manager.change_weekly_limit()

while True:
    print("1. Add Expense")
    print("2. Reset Weekly Budget")
    print("3. Show List of Expenses")
    print("4. Show Limit Left")
    print("5. Change Weekly Limit")
    print("6. Set Category Limits")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        budget_manager.add_expense()
    elif choice == '2':
        budget_manager.reset_weekly_budget()
    elif choice == '3':
        budget_manager.show_expenses()
    elif choice == '4':
        budget_manager.check_budget()
    elif choice == '5':
        budget_manager.change_weekly_limit()
    elif choice == '6':
        budget_manager.set_category_limits()
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please try again.")
