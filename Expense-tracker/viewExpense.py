FILE_NAME = "expenses.txt"


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

            if not lines:
                print("\nNo expenses found.\n")
                return

            print("\nDate        Amount         Category              Description")
            print("----------------------------------------------------------------")

            for line in lines:
                date, amount, category, desc = line.strip().split("|")
                print(f"{date}   {amount:<12}  {category:<20}  {desc}")

            print()

    except FileNotFoundError:
        print("\nExpense file not found.\n")
