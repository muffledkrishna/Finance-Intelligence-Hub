import pandas as pd

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

all_margins = []

for company in companies:

    df = pd.read_csv(
        f"data/{company}_financials.csv",
        index_col=0
    )

    if (
        "Total Revenue" in df.index
        and
        "Net Income" in df.index
    ):

        revenue_row = df.loc["Total Revenue"]
        income_row = df.loc["Net Income"]

        for year in revenue_row.index:

            revenue = revenue_row[year]
            income = income_row[year]

            if pd.notna(revenue) and revenue != 0:

                margin = (
                    income / revenue
                ) * 100

                all_margins.append({
                    "Company": company,
                    "Year": year,
                    "Revenue": revenue,
                    "NetIncome": income,
                    "NetMargin": round(
                        margin,
                        2
                    )
                })

margins_df = pd.DataFrame(
    all_margins
)

margins_df.to_csv(
    "data/margins.csv",
    index=False
)

print(
    "margins.csv created!"
)

print(
    margins_df.head()
)