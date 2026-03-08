from binance.client import Client
import numpy as np
import time

API_KEY = "8AQE2uHEC7qfmHtMSXiTxMZz5aEkJe9rCBo4v9SKodkYXzbKlqF3mpl5XOLmoKTx"
API_SECRET = "YYoNUsBjCBhY52gWpyBH9WfuVd3gn0G0ruRDdRvyrIIGAlrvhqvLG73Xh0VkFZSo"

SYMBOL = "BTCUSDT"
LEVERAGE = 3
GRID_COUNT = 15
LOWER_PRICE = 40000
UPPER_PRICE = 46000
QTY = 0.001

client = Client(AQE2uHEC7qfmHtMSXiTxMZz5aEkJe9rCBo4v9SKodkYXzbKlqF3mpl5XOLmoKTx, YYoNUsBjCBhY52gWpyBH9WfuVd3gn0G0ruRDdRvyrIIGAlrvhqvLG73Xh0VkFZSo)
client.futures_change_leverage(symbol=SYMBOL, leverage=LEVERAGE)

grid = np.linspace(LOWER_PRICE, UPPER_PRICE, GRID_COUNT)

print("Futures Grid Bot Started...")

def buy(price):
    client.futures_create_order(
        symbol=SYMBOL,
        side="BUY",
        type="LIMIT",
        timeInForce="GTC",
        quantity=QTY,
        price=round(price, 2)
    )

for p in grid:
    try:
        buy(p)
        time.sleep(0.3)
    except Exception as e:
        print(e)

while True:
    time.sleep(5)
