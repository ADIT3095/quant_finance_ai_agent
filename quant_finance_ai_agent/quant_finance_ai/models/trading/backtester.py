def backtest(prices, signals):
    returns = prices.pct_change().shift(-1)
    strategy_returns = returns * signals.shift(1)
    return strategy_returns.cumsum()
