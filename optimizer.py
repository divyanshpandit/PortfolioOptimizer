
import pandas as pd
import matplotlib.pyplot as plt
import argparse

def load_assets(file):
    df = pd.read_csv(file)
    df['ExpectedReturn'] = df['ExpectedReturn(%)'] / 100
    df['Risk'] = df['Risk(%)'] / 100
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    df.dropna(inplace=True)
    return df

def knapsack_dp(assets, capital):
    n = len(assets)
    W = int(capital)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    selected = [[[] for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        price = int(assets.iloc[i-1]['Price'])
        ret = assets.iloc[i-1]['ExpectedReturn']
        for w in range(W + 1):
            if price <= w:
                if dp[i-1][w - price] + ret > dp[i-1][w]:
                    dp[i][w] = dp[i-1][w - price] + ret
                    selected[i][w] = selected[i-1][w - price] + [i-1]
                else:
                    dp[i][w] = dp[i-1][w]
                    selected[i][w] = selected[i-1][w]
            else:
                dp[i][w] = dp[i-1][w]
                selected[i][w] = selected[i-1][w]
    return selected[n][W]

def calculate_portfolio_metrics(assets, indices):
    subset = assets.iloc[indices]
    total_return = subset['ExpectedReturn'].sum()
    avg_risk = subset['Risk'].mean()
    tickers = list(subset['Ticker'])
    return tickers, total_return, avg_risk

def efficient_frontier(assets, capital):
    risk_vals = [x / 100 for x in range(0, 100, 5)]
    points = []

    for risk_tol in risk_vals:
        chosen = knapsack_dp(assets[assets['Risk'] <= risk_tol], capital)
        if not chosen:
            continue
        tickers, ret, risk = calculate_portfolio_metrics(assets, chosen)
        points.append((risk, ret))
    return points

def plot_frontier(points, filename='frontier.png'):
    x, y = zip(*points)
    plt.plot(x, y, marker='o')
    plt.xlabel("Risk")
    plt.ylabel("Return")
    plt.title("Efficient Frontier")
    plt.grid(True)
    plt.savefig(filename)
    print(f"Frontier plot saved to {filename}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--capital', type=float, required=True)
    parser.add_argument('--risk', type=float, required=True)
    parser.add_argument('--csv', type=str, required=True)
    args = parser.parse_args()

    assets = load_assets(args.csv)
    filtered = assets[assets['Risk'] <= args.risk / 100]
    chosen = knapsack_dp(filtered, args.capital)

    if not chosen:
        print("No portfolio matches the given constraints.")
        return

    tickers, ret, risk = calculate_portfolio_metrics(assets, chosen)
    print(f"Selected {len(tickers)} assets:")
    print("Tickers:", ", ".join(tickers))
    print(f"Total Return: {ret*100:.2f}%")
    print(f"Avg Risk: {risk*100:.2f}%")

    # Frontier
    points = efficient_frontier(assets, args.capital)
    plot_frontier(points)

if __name__ == "__main__":
    main()
