import yfinance as yf
import os

companies = [
    "AAPL","MSFT","GOOGL","AMZN",
    "NVDA","META","JPM","BAC",
    "WMT","COST","XOM","JNJ"
]

os.makedirs("data", exist_ok=True)

for ticker in companies:

    try:

        stock = yf.Ticker(ticker)

        balance_sheet = stock.balance_sheet

        balance_sheet.to_csv(
            f"data/{ticker}_balance_sheet.csv"
        )

        print(
            f"{ticker} balance sheet saved"
        )

    except Exception as e:

        print(
            f"Error with {ticker}: {e}"
        )