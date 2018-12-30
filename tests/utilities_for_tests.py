import pandas as pd
from PyPortfolioOpt.pypfopt import expected_returns
from PyPortfolioOpt.pypfopt import risk_models
from PyPortfolioOpt.pypfopt.efficient_frontier import EfficientFrontier


def get_data():
    return pd.read_csv("stock_prices.csv", parse_dates=True, index_col="date")

def setup_efficient_frontier(data_only=False):
    df = get_data()
    mean_return = expected_returns.mean_historical_return(df)
    sample_cov_matrix = risk_models.sample_cov(df)
    if data_only:
        return mean_return, sample_cov_matrix
    return EfficientFrontier(mean_return, sample_cov_matrix)


