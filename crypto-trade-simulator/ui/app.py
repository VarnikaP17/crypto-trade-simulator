import sys
import os
import time
import streamlit as st

# Add parent directory to path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import project modules
from websocket_client import OrderBookWebSocket
from models.slippage import estimate_slippage
from models.market_impact import estimate_market_impact
from models.maker_taker import estimate_maker_taker_ratio
from models.fee import estimate_fee  # You must implement this

# Streamlit page setup
st.set_page_config(page_title="Crypto Trade Simulator", layout="wide")
st.title("📈 Real-time Crypto Trade Simulator")

# --- Sidebar Inputs ---
st.sidebar.header("Trade Parameters")

symbol = st.sidebar.selectbox("Select Symbol", ["BTC-USDT-SWAP"])  # Extendable
quantity = st.sidebar.number_input("Order Quantity (USD)", min_value=1.0, value=100.0)
volatility = st.sidebar.slider("Market Volatility (%)", min_value=0.1, max_value=10.0, value=1.5)
fee_tier = st.sidebar.selectbox("Fee Tier", ["Tier 1", "Tier 2"])

start = st.sidebar.button("Start Feed")

# --- Right Panel Output ---
col1, col2 = st.columns(2)
orderbook_box = col1.empty()
results_box = col2.empty()

# --- WebSocket Feed Start ---
if start:
    st.sidebar.success("WebSocket stream started.")
    ob = OrderBookWebSocket(symbol)
    ob.run()

    start_tick = time.time()

    try:
        while True:
            orderbook = ob.get_orderbook()

            if orderbook and orderbook["bids"] and orderbook["asks"]:
                best_bid = orderbook["bids"][0]
                best_ask = orderbook["asks"][0]

                # --- Display Order Book ---
                orderbook_box.markdown(f"### 🧾 Order Book - {symbol}")
                orderbook_box.write(f"**Best Bid:** ${best_bid[0]:,.2f} (Qty: {best_bid[1]})")
                orderbook_box.write(f"**Best Ask:** ${best_ask[0]:,.2f} (Qty: {best_ask[1]})")

                # --- Estimates ---
                slippage = estimate_slippage(orderbook, quantity)
                fee = estimate_fee(quantity, fee_tier)
                impact = estimate_market_impact(quantity, volatility)
                net_cost = slippage + fee + impact

                maker_prob, taker_prob = estimate_maker_taker_ratio(orderbook, quantity)

                # --- Display Results ---
                results_box.markdown("### 📊 Estimated Costs")
                results_box.write(f"🔻 **Slippage**: ${slippage:.4f}")
                results_box.write(f"💸 **Fee**: ${fee:.4f}")
                results_box.write(f"📉 **Market Impact**: ${impact:.4f}")
                results_box.success(f"📦 **Net Transaction Cost**: ${net_cost:.4f}")

                results_box.write(f"🧠 **Maker Probability**: {maker_prob:.2%}")
                results_box.write(f"⚡ **Taker Probability**: {taker_prob:.2%}")

                latency_ms = (time.time() - start_tick) * 1000
                results_box.write(f"⏱️ **Latency**: {latency_ms:.2f} ms")

            time.sleep(1)

    except KeyboardInterrupt:
        st.warning("Stream stopped manually.")

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
