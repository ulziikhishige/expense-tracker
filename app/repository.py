from datetime import date, datetime
from app.database import db_session
from app.models import Expense


class ExpenseRepository:

    def add_expense(
        self,
        user_id: int,
        category_id: int,
        amount: float,
        description: str,
        expense_date: date,
    ) -> None:
        with db_session() as conn:
            conn.execute(
                """
                INSERT INTO expenses (
                    user_id,
                    category_id,
                    amount,
                    description,
                    expense_date,
                    created_at
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    user_id,
                    category_id,
                    amount,
                    description,
                    expense_date.isoformat(),
                    datetime.utcnow().isoformat(),
                ),
            )

    def list_by_month(
        self,
        user_id: int,
        year: int,
        month: int,
    ) -> list[Expense]:
        month_str = f"{year}-{month:02d}"

        with db_session() as conn:
            rows = conn.execute(
                """
                SELECT
                    e.amount,
                    c.name AS category,
                    e.description,
                    e.expense_date
                FROM expenses e
                JOIN categories c ON e.category_id = c.id
                WHERE e.user_id = ?
                  AND e.expense_date LIKE ?
                ORDER BY e.expense_date
                """,
                (user_id, f"{month_str}%"),
            ).fetchall()

        return [
            Expense(
                amount=row["amount"],
                category=row["category"],
                description=row["description"],
                date=date.fromisoformat(row["expense_date"]),
            )
            for row in rows
        ]

    def category_summary(
        self,
        user_id: int,
        year: int,
        month: int,
    ) -> dict[str, float]:
        month_str = f"{year}-{month:02d}"

        with db_session() as conn:
            rows = conn.execute(
                """
                SELECT
                    c.name AS category,
                    SUM(e.amount) AS total
                FROM expenses e
                JOIN categories c ON e.category_id = c.id
                WHERE e.user_id = ?
                  AND e.expense_date LIKE ?
                GROUP BY c.name
                """,
                (user_id, f"{month_str}%"),
            ).fetchall()

        return {row["category"]: row["total"] for row in rows}
