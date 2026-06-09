import yfinance as yf
import pandas as pd
import os

companies = [
    "AAPL",
    "MSFT",
    "GOOGL",
    "AMZN",
    "NVDA",
    "META",
    "JPM",
    "BAC",
    "WMT",
    "COST",
    "XOM",
    "JNJ"
]

os.makedirs("data", exist_ok=True)

for ticker in companies:

    print(f"Downloading {ticker}...")

    try:

        stock = yf.Ticker(ticker)

        financials = stock.financials

        financials.to_csv(
            f"data/{ticker}_financials.csv"
        )

        print(f"{ticker} saved successfully")

    except Exception as e:

        print(f"Error with {ticker}")
        print(e)

print("\nDownload Complete!")