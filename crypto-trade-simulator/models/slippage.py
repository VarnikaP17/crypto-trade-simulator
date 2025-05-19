# models/slippage.py
def estimate_slippage(orderbook, quantity):
    depth = 0
    filled = 0
    slippage = 0

    for price, size in orderbook["asks"]:
        size_usd = price * size
        if filled + size_usd >= quantity:
            slippage += price * ((quantity - filled) / price)
            break
        else:
            filled += size_usd
            slippage += price * size

    avg_price = slippage / (quantity / price)
    top_price = orderbook["asks"][0][0]
    return avg_price - top_price  # difference from top of book

# models/slippage.py

def estimate_slippage(orderbook, quantity_usd):
    """Linear slippage estimate based on top ask depth"""
    if not orderbook["asks"]:
        return 0.0

    total_qty = 0
    total_cost = 0
    target_qty = quantity_usd
    for price_str, size_str in orderbook["asks"]:
        price = float(price_str)
        size = float(size_str)
        trade_value = price * size

        if total_qty + trade_value >= target_qty:
            needed = (target_qty - total_qty) / price
            total_cost += needed * price
            break
        else:
            total_cost += trade_value
            total_qty += trade_value

    avg_price = total_cost / (target_qty / float(orderbook["asks"][0][0]))
    slippage = avg_price - float(orderbook["asks"][0][0])
    return slippage

def estimate_fee(quantity_usd, fee_tier="Tier 1"):
    fee_percent = {
        "Tier 1": 0.001,  # 0.1%
        "Tier 2": 0.0008, # 0.08%
    }
    return quantity_usd * fee_percent.get(fee_tier, 0.001)
