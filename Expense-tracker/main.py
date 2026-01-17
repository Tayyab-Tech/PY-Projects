from datetime import datetime
from viewExpense import view_expenses
from summaryCat import category_summary_and_highest
from monthlyExpense import monthly_expense
from dateRange import date_range_filter
from addExpense import add_expense,get_valid_date
from delExpense import delete_expense
from updateExpense import update_expense

FILE_NAME = "expenses.txt"


def total_expense():
    total = 0.0

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                total += float(line.strip().split("|")[1])

        print(f"\nTotal Expense: {total}\n")

    except FileNotFoundError:
        print("Expense file not found.\n")


# ---------- Menu ----------

def menu():
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Expense")
        print("4. Monthly Expense Report")
        print("5. Category Summary + Highest Spending")
        print("6. Filter Expenses by Date Range")
        print("7. Update Expense")
        print("8. Delete Expense")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            monthly_expense()
        elif choice == "5":
            category_summary_and_highest()
        elif choice == "6":
            date_range_filter()
        elif choice == "7":
            update_expense()
        elif choice == "8":
            delete_expense()
        elif choice == "0":
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")


menu()
