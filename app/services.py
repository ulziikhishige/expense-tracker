from datetime import date
from app.models import Expense
from app.repository import ExpenseRepository


class ExpenseService:
    def __init__(self, repo: ExpenseRepository):
        self.repo = repo

    def add_expense(
        self,
        user_id: int,
        category_id: int,
        amount: float,
        description: str,
        expense_date: date,
    ) -> None:
        # 🔒 Business rules
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if expense_date > date.today():
            raise ValueError("Expense date cannot be in the future")

        self.repo.add_expense(
            user_id=user_id,
            category_id=category_id,
            amount=amount,
            description=description,
            expense_date=expense_date,
        )

    def get_monthly_expenses(
        self,
        user_id: int,
        year: int,
        month: int,
    ) -> list[Expense]:
        if not (1 <= month <= 12):
            raise ValueError("Invalid month")

        return self.repo.list_by_month(
            user_id=user_id,
            year=year,
            month=month,
        )

    def get_category_summary(
        self,
        user_id: int,
        year: int,
        month: int,
    ) -> dict[str, float]:
        expenses = self.repo.category_summary(
            user_id=user_id,
            year=year,
            month=month,
        )

        if not expenses:
            raise ValueError("No expenses found for this period")

        return expenses
