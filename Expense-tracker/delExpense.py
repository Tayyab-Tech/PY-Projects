FILE_NAME = "expenses.txt"


def delete_expense():
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        if not lines:
            print("\nNo expenses to delete.\n")
            return

        print("\nSelect expense to delete:\n")
        for i, line in enumerate(lines): # return index with the element
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

        confirm = input(
            f"\nAre you sure you want to delete this expense? (y/n): "
        ).lower()

        if confirm != "y":
            print("\nDelete cancelled.\n")
            return

        deleted = lines.pop(index)

        with open(FILE_NAME, "w") as file:
            file.writelines(lines)

        print("\nExpense deleted successfully.\n")

    except FileNotFoundError:
        print("\nExpense file not found.\n")
