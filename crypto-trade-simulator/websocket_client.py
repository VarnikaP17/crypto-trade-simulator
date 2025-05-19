# websocket_client.py
import websocket
import json
import threading
import time

class OrderBookWebSocket:
    def __init__(self, symbol="BTC-USDT-SWAP"):
        self.symbol = symbol
        self.orderbook = {"bids": [], "asks": []}
        self.ws = None

    def on_message(self, ws, message):
        data = json.loads(message)
        if "bids" in data and "asks" in data:
            self.orderbook = {
                "bids": [(float(price), float(size)) for price, size in data["bids"]],
                "asks": [(float(price), float(size)) for price, size in data["asks"]],
            }

    def on_open(self, ws):
        print(f"Connected to OKX for {self.symbol}")

    def run(self):
        def _run():
            self.ws = websocket.WebSocketApp(
                f"wss://ws.gomarket-cpp.goquant.io/ws/l2-orderbook/okx/{self.symbol}",
                on_open=self.on_open,
                on_message=self.on_message
            )
            self.ws.run_forever()

        thread = threading.Thread(target=_run)
        thread.daemon = True
        thread.start()

    def get_orderbook(self):
        return self.orderbook
