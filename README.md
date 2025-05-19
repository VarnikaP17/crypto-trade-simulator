# Real-Time Cryptocurrency Trade Simulator

This project is a real-time cryptocurrency trade simulator designed to analyze the market impact, slippage, and latency of large trades. It connects to live L2 (Level 2) order book data from OKX using WebSockets and simulates trade execution using both empirical and theoretical modeling techniques.

## 📂 Folder Structure

crypto-trade-simulator/
├── src/ # Source code for simulator logic
├── models/ # Regression and Almgren-Chriss models
├── data/ # Historical data samples (if any)
├── utils/ # Utility modules for parsing, metrics, etc.
├── ui/ # Optional UI components (React/Dash/CLI)
├── README.md # Project documentation
└── requirements.txt # Python dependencies

---

## 📊 Model Selection and Parameters

### Regression Models
- **Linear Regression**: For modeling average price movement per trade size.
- **Polynomial Regression (Degree 2/3)**: To capture nonlinear impact at higher volumes.
- **Lasso/Ridge Regression**: Used to regularize and prevent overfitting on historical order book features.

### Almgren-Chriss Model
- A theoretical model that balances **market impact** with **risk aversion** and **execution time**.
- Parameters used:
  - Risk aversion parameter (`λ`)
  - Volatility (`σ`)
  - Average daily volume (`ADV`)
  - Permanent and temporary impact coefficients (`η`, `γ`)

---

## 📈 Regression Techniques Chosen

1. **Empirical Regression**:
   - Based on historical or real-time L2 order book snapshots.
   - Feature set includes: `mid_price`, `order_depth`, `spread`, `volume_imbalance`, etc.

2. **Execution Slippage Estimation**:
   - Slippage = (Executed Price - Mid Price) / Mid Price
   - Regressed as a function of `order size`, `spread`, and `book depth`.

3. **Cross-Validation**:
   - K-fold and time-series split used to tune hyperparameters for model generalization.

---

## 📉 Market Impact Calculation Methodology

### Direct Simulation
- Trades are virtually executed against the real-time order book.
- Market impact is measured as the change in mid-price before and after execution.

### Almgren-Chriss Analytical Approach
- Execution is broken into `N` slices.
- Each slice models:
  - Temporary impact = `η * v`
  - Permanent impact = `γ * cumulative_volume`
- Price trajectory is derived analytically and compared against real execution data.

---

## 🚀 Performance Optimization Approaches

- **WebSocket Buffering**:
  - Efficient real-time order book updates using delta merge strategies.
- **Numpy/Numba Acceleration**:
  - Vectorized calculations for slippage and impact metrics.
- **Batch Execution**:
  - Trade simulations are parallelized to reduce runtime latency.
- **Lazy Loading & Caching**:
  - Order book snapshots are cached and compressed for quick re-use.
- **UI Performance**:
  - Only delta diffs are sent to the frontend to reduce bandwidth and latency.

---

## 📦 Deliverables

1. ✅ Complete source code with full inline documentation
2. ✅ Jupyter Notebooks for model training and evaluation
3. ✅ CLI or Web UI for running and visualizing simulations
4. ✅ Configurable parameters for:
   - Trade size
   - Time intervals
   - Risk aversion
   - Exchange selection (currently OKX)

---

## 🔧 Setup Instructions

```bash
# Clone the repository
git clone  https://github.com/VarnikaP17/crypto-trade-simulator.git
cd crypto-trade-simulator

# Install dependencies
pip install -r requirements.txt

# Start simulator
python src/main.py
