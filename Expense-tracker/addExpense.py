from datetime import datetime
FILE_NAME = "expenses.txt"


# ---------- Validation Helpers ----------

def get_valid_date():
    while True:
        date_input = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.\n")

#---------- Add Expense ---------------

def add_expense():
    date = get_valid_date()

    # ---------- Categories ----------
    category_input = input(
        "Enter categories (comma separated): "
    ).strip()

    categories = [c.strip().title() for c in category_input.split(",") if c.strip()]

    if not categories:
        print("\nCategory cannot be empty.\n")
        return

    # ---------- Amounts ----------
    amount_input = input(
        "Enter amounts (comma separated): "
    ).strip()

    try:
        amounts = [float(a.strip()) for a in amount_input.split(",") if a.strip()]
    except ValueError:
        print("\nAll amounts must be valid numbers.\n")
        return

    if not amounts or any(a <= 0 for a in amounts):
        print("\nEach amount must be greater than 0.\n")
        return

    # ---------- Descriptions ----------
    desc_input = input(
        "Enter descriptions (comma separated): "
    ).strip()

    descriptions = [d.strip().capitalize() for d in desc_input.split(",") if d.strip()]

    if not descriptions:
        print("\nDescription cannot be empty.\n")
        return

    # ---------- COUNT CHECK ----------
    if not (len(categories) == len(amounts) == len(descriptions)):
        print(
            f"\nError: Categories({len(categories)}), "
            f"Amounts({len(amounts)}), "
            f"Descriptions({len(descriptions)})\n"
            "All three counts must be exactly the same.\n"
        )
        return

    # ---------- Save ----------
    with open(FILE_NAME, "a") as file:
        for cat, amt, desc in zip(categories, amounts, descriptions): # combine same index in tuple from multiple lists
            file.write(f"{date}|{amt}|{cat}|{desc}\n")

    print("\nExpenses added successfully (fully mapped & validated).\n")
