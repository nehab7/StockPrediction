import yfinance as yf
import os

tickers = ["AAPL", "TSLA", "MSFT"]

for ticker in tickers:
    df = yf.download(ticker, start="2019-01-01", end="2025-03-31")
    df.to_csv(f"StockPrediction/price/{ticker}.csv")
    print(f"Saved: {ticker}")
