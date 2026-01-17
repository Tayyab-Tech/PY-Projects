FILE_NAME = "expenses.txt"


def monthly_expense():
    monthly_totals = {}

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                date, amount, category, desc = line.strip().split("|")
                month = date[:7]  # YYYY-MM [1:]
                amount = float(amount)

                monthly_totals[month] = monthly_totals.get(month, 0) + amount

        if not monthly_totals:
            print("No expenses found.\n")
            return

        print("\nMonthly Expense Report")
        print("----------------------")
        for month, total in monthly_totals.items():
            print(f"{month}: {total}")

        print()

    except FileNotFoundError:
        print("Expense file not found.\n")
