from datetime import datetime

FILE_NAME = "expenses.txt"


def date_range_filter():
    # User se start aur end date lein
    while True:
        start_date_input = input("Enter start date (YYYY-MM-DD): ")
        try:
            start_date = datetime.strptime(start_date_input, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    while True:
        end_date_input = input("Enter end date (YYYY-MM-DD): ")
        try:
            end_date = datetime.strptime(end_date_input, "%Y-%m-%d")
            if end_date < start_date:
                print("\nEnd date cannot be before start date.")
            else:
                break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    # Read expenses and filter
    filtered_expenses = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                date_str, amount, category, desc = line.strip().split("|")
                expense_date = datetime.strptime(date_str, "%Y-%m-%d")
                if start_date <= expense_date <= end_date:
                    filtered_expenses.append((date_str, amount, category, desc))

        if not filtered_expenses:
            print("\nNo expenses found in this date range.\n")
            return

        print("\nExpenses from {} to {}".format(start_date_input, end_date_input))
        print("Date        Amount    Category       Description")
        print("------------------------------------------------")
        total_amount = 0
        for date_str, amount, category, desc in filtered_expenses:
            print(f"{date_str}   {amount:<8}  {category:<13}  {desc}")
            total_amount += float(amount)
        print(f"\nTotal Expense in this range: {total_amount}\n")

    except FileNotFoundError:
        print("Expense file not found.\n")
