
import unittest
import pandas as pd
from optimizer import load_assets, knapsack_dp, calculate_portfolio_metrics

class TestPortfolioOptimizer(unittest.TestCase):

    def setUp(self):
        self.assets = pd.DataFrame({
            "Ticker": ["A", "B", "C", "D", "E"],
            "ExpectedReturn(%)": [10, 20, 30, 40, 50],
            "Risk(%)": [5, 10, 15, 20, 25],
            "Sector": ["X"] * 5,
            "Price": [100, 200, 300, 400, 500]
        })
        self.assets['ExpectedReturn'] = self.assets['ExpectedReturn(%)'] / 100
        self.assets['Risk'] = self.assets['Risk(%)'] / 100

    def test_knapsack_selection(self):
        selected_indices = knapsack_dp(self.assets, 500)
        self.assertTrue(isinstance(selected_indices, list))
        self.assertTrue(all(isinstance(i, int) for i in selected_indices))

    def test_portfolio_metrics(self):
        indices = [0, 1]  # Assets A and B
        tickers, total_return, avg_risk = calculate_portfolio_metrics(self.assets, indices)
        self.assertEqual(tickers, ["A", "B"])
        self.assertAlmostEqual(total_return, 0.30)
        self.assertAlmostEqual(avg_risk, 0.075)

if __name__ == "__main__":
    unittest.main()
