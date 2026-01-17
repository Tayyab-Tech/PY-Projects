from datetime import datetime
from addExpense import get_valid_date
FILE_NAME = "expenses.txt"


def update_expense():
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        if not lines:
            print("\nNo expenses to update.\n")
            return

        print("\nSelect expense to update:\n")
        for i, line in enumerate(lines):
            date, amount, cat, desc = line.strip().split("|")
            print(f"{i + 1}. {date} | {amount} | {cat} | {desc}")

        choice = input("\nEnter expense number: ").strip()
        if not choice.isdigit():
            print("\nInvalid input.\n")
            return

        index = int(choice) - 1
        if index < 0 or index >= len(lines):
            print("\nInvalid expense number.\n")
            return

        print("\nEnter new values:")

        date = get_valid_date()

        # ---------- Amounts ----------
        amount_input = input("Enter amounts (comma separated): ").strip()
        try:
            amounts = [float(a.strip()) for a in amount_input.split(",") if a.strip()]
        except ValueError:
            print("\nAll amounts must be valid numbers.\n")
            return

        if not amounts or any(a <= 0 for a in amounts):
            print("\nEach amount must be greater than 0.\n")
            return

        # ---------- Categories ----------
        cat_input = input("Enter categories (comma separated): ").strip()
        categories = [c.strip().title() for c in cat_input.split(",") if c.strip()]

        # ---------- Descriptions ----------
        desc_input = input("Enter descriptions (comma separated): ").strip()
        descriptions = [d.strip().capitalize() for d in desc_input.split(",") if d.strip()]

        # ---------- STRICT COUNT CHECK ----------
        if not (len(amounts) == len(categories) == len(descriptions)):
            print(
                f"\nError: Amounts({len(amounts)}), "
                f"Categories({len(categories)}), "
                f"Descriptions({len(descriptions)}) must be equal.\n"
            )
            return

        # ---------- Remove old line ----------
        lines.pop(index)

        # ---------- Insert updated records ----------
        for amt, cat, desc in zip(amounts, categories, descriptions):
            lines.append(f"{date}|{amt}|{cat}|{desc}\n")

        with open(FILE_NAME, "w") as file:
            file.writelines(lines)

        print("\nExpense updated successfully (expanded into multiple records).\n")

    except FileNotFoundError:
        print("\nExpense file not found.\n")
