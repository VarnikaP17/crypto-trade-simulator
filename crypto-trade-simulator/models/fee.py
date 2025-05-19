# models/fee.py

def estimate_fee(quantity_usd, fee_tier):
    """
    Estimate transaction fee based on fee tier and notional quantity (in USD).
    
    Args:
        quantity_usd (float): Order size in USD.
        fee_tier (str): Selected fee tier ("Tier 1", "Tier 2", etc.)

    Returns:
        float: Estimated fee in USD
    """

    # Example fee rates (real-world tiers may vary slightly)
    fee_rates = {
        "Tier 1": 0.001,  # 0.10%
        "Tier 2": 0.0005,  # 0.05%
    }

    fee_rate = fee_rates.get(fee_tier, 0.001)  # Default to Tier 1 if not found
    return quantity_usd * fee_rate
