from datetime import date
from app.services import ExpenseService
from app.repository import ExpenseRepository


def prompt_add_expense(service: ExpenseService):
    try:
        amount = float(input("Amount: "))
        category_id = int(input("Category ID: "))
        description = input("Description: ")
        expense_date = date.fromisoformat(
            input("Date (YYYY-MM-DD): ")
        )

        service.add_expense(
            user_id=1,
            category_id=category_id,
            amount=amount,
            description=description,
            expense_date=expense_date,
        )
        print("✅ Expense added")

    except Exception as e:
        print(f"❌ Error: {e}")


def prompt_monthly_report(service: ExpenseService):
    try:
        year = int(input("Year: "))
        month = int(input("Month (1-12): "))

        expenses = service.get_monthly_expenses(
            user_id=1,
            year=year,
            month=month,
        )

        print("\n--- Monthly Expenses ---")
        for e in expenses:
            print(f"{e.date} | {e.category:<10} | ¥{e.amount} | {e.description}")

    except Exception as e:
        print(f"❌ Error: {e}")


def run_cli():
    repo = ExpenseRepository()
    service = ExpenseService(repo)

    while True:
        print("\n1. Add expense")
        print("2. Monthly report")
        print("0. Exit")

        choice = input("Select: ")

        if choice == "1":
            prompt_add_expense(service)
        elif choice == "2":
            prompt_monthly_report(service)
        elif choice == "0":
            print("Bye 👋")
            break
        else:
            print("Invalid option")
