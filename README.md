# Budget_Manager_Python_App

## Introduction
The Budget Manager is a simple and efficient tool designed to help you manage your weekly budget. This program allows you to categorize your expenses, track your spending, and ensure you stay within your budget limits. The Budget Manager is implemented in Python and uses CSV files to store and manage your expense data.

## Features
- **Add Expenses**: Categorize and add your daily expenses.
- **Weekly Budget Limit**: Set and update your weekly budget limit.
- **Expense Tracking**: Keep track of your spending in various categories.
- **Budget Alerts**: Receive alerts when you exceed your weekly budget.
- **Reset Weekly Budget**: Reset your budget at the end of each week.
- **Save and Load Data**: Save your expense data to a CSV file and load it on startup.
- **Set Category Limits**: Customize spending limits for each category.

## Categories
The Budget Manager categorizes expenses into the following categories:
1. Food and Groceries
2. Transportation
3. Healthcare
4. Savings and Emergency Fund
5. Entertainment
6. Personal Care
7. Miscellaneous

## Usage
1. **Initialize Budget Manager**:
   - Run the program and enter your weekly budget limit.
   
2. **Main Menu**:
   - Add Expense
   - Reset Weekly Budget
   - Show List of Expenses
   - Show Limit Left
   - Change Weekly Limit
   - Set Category Limits
   - Exit

3. **Add Expense**:
   - Select a category and enter the amount.
   - The expense will be added to the specified category and saved to the CSV file.

4. **Reset Weekly Budget**:
   - Reset the budget at the end of each week to start fresh.

5. **Show List of Expenses**:
   - Display the list of expenses for each category and the remaining limit.

6. **Show Limit Left**:
   - Check the total amount spent and the remaining budget.

7. **Change Weekly Limit**:
   - Update your weekly budget limit and adjust category limits accordingly.

8. **Set Category Limits**:
   - Customize the spending limits for each category.

## How to Run
1. **Install Python**: Ensure Python is installed on your system.
2. **Save the Code**: Save the provided code to a file named `budget_manager.py`.
3. **Run the Program**: Open a terminal or command prompt and run the program using the command:
   ```sh
   python budget_manager.py
   ```

## Dependencies
- Python 3.x
- CSV module (builtin)
- Datetime module (builtin)
- OS module (builtin)

## Notes
- The initial weekly limit is set to 0. Please update the weekly limit before adding expenses.
- Ensure the `budget_passbook.csv` file is in the same directory as the program.
