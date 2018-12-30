import numpy as np
from PyPortfolioOpt.pypfopt.hierarchical_risk_parity import hrp_portfolio
from PyPortfolioOpt.tests.utilities_for_tests import get_data


def test_hrp_portfolio():
    df = get_data()

    returns = df.pct_change().dropna(how="all")
    print returns
    w = hrp_portfolio(returns)
    print w
    assert isinstance(w, dict)
    assert set(w.keys()) == set(df.columns)
    np.testing.assert_almost_equal(sum(w.values()), 1)


test_hrp_portfolio()