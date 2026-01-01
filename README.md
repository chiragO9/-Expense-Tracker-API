# 💰 Expense Tracker API

A RESTful API for tracking personal income and expenses built with FastAPI and Python.

## Features

- Track income and expenses
- Categorize transactions
- View financial summaries
- Filter by category and type
- CRUD operations for all expense entries

## Tech Stack

- **Framework:** FastAPI
- **Language:** Python 3.11+
- **Database:** MySQL (planned)
- **Authentication:** JWT (planned)

## API Endpoints

### Expenses
- `GET /expenses` - Get all expenses
- `GET /expenses/{id}` - Get specific expense 
- `POST /expenses` - Create new expense (Pending)
- `PUT /expenses/{id}` - Update expense  (Pending)
- `DELETE /expenses/{id}` - Delete expense  (Pending)

### Summary
- `GET /summary` - Get financial overview 
- `GET /categories` - Get all categories (Pending)

### Prerequisites
```bash
Python 3.11+
pip
```

### Installation

1. Clone the repository
```bash
git clone https://github.com/chiragO9/expense-tracker-api.git
cd expense-tracker-api
```

2. Install dependencies
```bash
pip install fastapi uvicorn 
```

3. Run the application
```bash
uvicorn main:app --reload
```

4. Open your browser and navigate to:
- API Docs: `http://localhost:8000/docs`
- API: `http://localhost:8000`

## 📝 Example Usage

### Create an Expense
```json
POST /expenses
{
  "amount": 500.50,
  "category": "Food",
  "description": "Grocery shopping",
  "date": "2026-01-15",
  "type": "expense"
}
```

### Get Summary
```json
GET /summary
{
  "total_income": 50000.00,
  "total_expenses": 14000.00,
  "balance": 36000.00
}
```

## 📚 Learning

This project is part of my learning journey with FastAPI. Built while following best practices for REST API development.


## Author

**Chirag Solanki**
- GitHub: [@chiragO9](https://github.com/chiragO9)

---
