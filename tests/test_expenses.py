def test_add_expense_negative_amount():
    with pytest.raises(ValueError):
        add_expense(repo, Expense(-10, "food", "", date.today()))
