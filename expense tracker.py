import os

expenses = "expenses.txt"

def initialize():
    if not os.path.exists(expenses):
        with open(expenses, 'w') as file:
            pass

def add():
    items = input("Enter the items: ")
    date = input("Date (YYYY-MM-DD): ")
    amt = input("Enter the expense amount: ")

    with open(expenses, 'a') as file:  # Changed to 'a' to append
        file.write(f"{items}, {date}, {amt}\n")
    print("Expense added successfully.")

def view():
    if os.stat(expenses).st_size == 0:
        print("No expenses available.")
        return

    with open(expenses, 'r') as file:
        expense_list = file.readlines()

    print("List of expenses:")
    for i, expense in enumerate(expense_list, start=1):
        items, date, amt = expense.strip().split(',')
        print(f"{i}. Items: {items}, Date: {date}, Amount: {amt}")

def delete():
    view()
    if os.stat(expenses).st_size == 0:
        return
    
    expense_number = int(input("Enter the number of the expense to delete: "))

    with open(expenses, 'r') as file:
        expense_list = file.readlines()

    if expense_number < 1 or expense_number > len(expense_list):
        print("Invalid expense number.")
        return
    
    del expense_list[expense_number - 1]

    with open(expenses, 'w') as file:
        file.writelines(expense_list)

    print("Expense deleted successfully.")

def view_total():
    if os.stat(expenses).st_size == 0:
        print("No expenses available.")
        return

    total = 0
    with open(expenses, 'r') as file:
        expense_list = file.readlines()

    for expense in expense_list:
        amt = expense.strip().split(',')[-1]  # Get the amount)
        total += float(amt)

    print(f"Total expenses: ${total:.2f}")

def main():
    while True:
        print("\nExpense Tracker:")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Delete an expense")
        print("4. View total expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add()
        elif choice == '2':
            view()
        elif choice == '3':
            delete()
        elif choice == '4':
            view_total()
        elif choice == '5':
            print("Thank you!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    initialize()
    main()
