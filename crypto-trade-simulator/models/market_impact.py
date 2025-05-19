# models/market_impact.py

def estimate_market_impact(quantity_usd, volatility_percent):
    """
    Estimate market impact cost using a simplified Almgren-Chriss style model.
    
    Args:
        quantity_usd (float): Trade size in USD.
        volatility_percent (float): Market volatility (as a percentage, e.g., 1.5).

    Returns:
        float: Estimated market impact in USD.
    """
    # Coefficients (mock values — tune as needed)
    gamma = 0.00005  # market impact factor
    volatility = volatility_percent / 100.0

    impact_cost = gamma * quantity_usd * volatility
    return round(impact_cost, 4)
