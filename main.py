from fastapi import FastAPI

app = FastAPI()

EXPENSES = [
  {
    'id' : 1,
    'amount' : 500,
    'category' : 'Food',
    'description' : 'Grocerry shopping',
    'date' : '1-1-2026',
    'type' : 'expense'
  },
 {
        'id': 2,
        'amount': 2000.00,
        'category': 'Transportation',
        'description': 'Monthly bus pass',
        'date': '2026-01-02',
        'type': 'expense'
    },
    {
        'id': 3,
        'amount': 50000.00,
        'category': 'Salary',
        'description': 'Monthly salary',
        'date': '2026-01-01',
        'type': 'income'
    },
    {
        'id': 4,
        'amount': 1500.00,
        'category': 'Entertainment',
        'description': 'Movie and dinner',
        'date': '2026-01-05',
        'type': 'expense'
    },
    {
        'id': 5,
        'amount': 12000.00,
        'category': 'Rent',
        'description': 'Monthly PG rent',
        'date': '2026-01-01',
        'type': 'expense'
    }
]



@app.get('/')
async def root():
  return {'message' : 'Welcome to the Expense Tracker API'}

@app.get('/expenses')
async def read_expenses():
  return EXPENSES 


@app.get('/expenses/{expense_id}')
async def read_expenses(expense_id : int):
  for expense in EXPENSES:
    if expense.get('id')  == expense_id:
      return expense
  return {'error : Expense not found'} 