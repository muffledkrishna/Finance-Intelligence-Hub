import pandas as pd

df = pd.read_csv(
    "data/AAPL_balance_sheet.csv",
    index_col=0
)

for row in df.index:

    if (
        "Equity" in row
        or
        "Debt" in row
    ):
        print(row)