# 📊 Portfolio Optimizer (0/1 Knapsack)

This project uses dynamic programming to optimize a stock portfolio based on capital and risk constraints. It visualizes the efficient frontier and helps in choosing the optimal subset of stocks.

## 🚀 Features

- Reads CSV market data (`assets.csv`)
- Applies 0/1 Knapsack dynamic programming for optimization
- Plots the efficient frontier (risk vs. return)
- Handles multiple constraints (capital, risk)
- Command-line interface
- Unit tested

## 📁 Files

- `optimizer.py` – Main logic and CLI interface
- `assets.csv` – Sample dataset (ticker, expected return, risk, price)
- `test_optimizer.py` – Unit tests for validation
- `frontier.png` – Output plot of the efficient frontier

## ⚙️ How to Run

```bash
python optimizer.py --capital 75000 --risk 36 --csv assets.csv

## Run Test
python -m unittest test_optimizer.py
