import yfinance as yf

def get_latest_price(ticker):
    data = yf.Ticker(ticker)
    return data.history(period="1d")['Close'].iloc[-1]
