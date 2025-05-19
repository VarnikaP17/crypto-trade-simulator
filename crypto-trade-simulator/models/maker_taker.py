# models/maker_taker.py

def estimate_maker_taker_ratio(orderbook, quantity_usd):
    """
    Dummy logic: Higher volume at top levels = higher taker likelihood.
    """
    top_ask_vol = float(orderbook["asks"][0][1])
    top_bid_vol = float(orderbook["bids"][0][1])
    total_vol = top_ask_vol + top_bid_vol

    if total_vol == 0:
        return 0.5  # undefined → neutral

    taker_prob = min(1.0, max(0.0, top_bid_vol / total_vol))
    maker_prob = 1.0 - taker_prob
    return round(maker_prob, 3), round(taker_prob, 3)
