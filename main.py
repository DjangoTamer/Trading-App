from fastapi import FastAPI

app = FastAPI(
    title='Trading App'
)

fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'investor', 'name': 'Alex'},
    {'id': 3, 'role': 'trader', 'name': 'Silva'},
]

fake_trades = [
    {'id': 1, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 123, 'amount': 2.12},
    {'id': 2, 'user_id': 1, 'currency': 'BTC', 'side': 'sell', 'price': 130, 'amount': 1.99},
    {'id': 3, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 128, 'amount': 2},
    {'id': 4, 'user_id': 1, 'currency': 'BTC', 'side': 'sell', 'price': 146, 'amount': 2},
    {'id': 5, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 140, 'amount': 3},
    {'id': 6, 'user_id': 1, 'currency': 'BTC', 'side': 'sell', 'price': 150, 'amount': 1},
    {'id': 7, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 146, 'amount': 1},
    {'id': 8, 'user_id': 1, 'currency': 'BTC', 'side': 'sell', 'price': 160, 'amount': 3},
    ]


@app.get('/users/{user_id}')
def get_user(user_id: int):
    return [i for i in fake_users if i['id'] == user_id]


@app.get('/trades')
def get_trades(limit: int = 3, offset: int = 0):
    return fake_trades[offset:offset + limit]


@app.post('/users/{user_id}')
def change_name(user_id: int, new_name: str):
    for i in fake_users:
        if i['id'] == user_id:
            i['name'] = new_name
    return fake_users
