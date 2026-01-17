FILE_NAME = "expenses.txt"


def category_summary_and_highest():
    category_totals = {}

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                date, amount, category, desc = line.strip().split("|")
                amount = float(amount)

                category_totals[category] = category_totals.get(category, 0) + amount

        if not category_totals:
            print("\nNo expenses found.\n")
            return

        print("\nCategory-wise Summary")
        print("---------------------")
        for cat, total in category_totals.items():
            print(f"{cat}: {total}")

        highest_category = max(category_totals, key=category_totals.get)
        print(
            f"\nHighest Spending Category: {highest_category} "
            f"({category_totals[highest_category]})\n"
        )

    except FileNotFoundError:
        print("\nExpense file not found.\n")
