def calculate_mid_price(bids, asks):
    if not bids or not asks:
        return None
    best_bid = float(bids[0][0])
    best_ask = float(asks[0][0])
    return (best_bid + best_ask) / 2
