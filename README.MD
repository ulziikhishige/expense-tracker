# 💰 Expense Tracker (Python + SQLite)

A simple but well-structured **CLI-based expense tracking application** built with Python and SQLite.  
This project focuses on clean architecture, separation of concerns, and practical backend fundamentals.

---

## 🚀 Features

- Add daily expenses
- Categorize expenses (food, rent, transport, gym, travel)
- Generate monthly expense reports
- SQLite database for persistence
- Modular architecture (database / services / CLI)
- Easy to extend to FastAPI or web backend

---

## 🧱 Project Structure

```
expense_tracker/
│
├── app/
│   ├── main.py          # CLI entry point
│   ├── database.py      # DB initialization & connection
│   ├── models.py        # Data models
│   ├── services.py      # Business logic
│   └── __init__.py
│
├── tests/               # Unit tests (pytest)
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1️⃣ Clone the repository

git clone https://github.com/ulziikhishige/expense-tracker.git
cd expense-tracker

### 2️⃣ Create virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

### 3️⃣ Install dependencies
pip install -r requirements.txt

### ▶️ How to Run
python -m app.main