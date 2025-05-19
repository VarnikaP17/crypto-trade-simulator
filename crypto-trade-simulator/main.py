# main.py
from websocket_client import OrderBookWebSocket
import time

client = OrderBookWebSocket()
client.run()

while True:
    orderbook = client.get_orderbook()
    print("Top Bid:", orderbook["bids"][0] if orderbook["bids"] else "Empty")
    print("Top Ask:", orderbook["asks"][0] if orderbook["asks"] else "Empty")
    time.sleep(1)
