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

kpis = []

for company in companies:

    df = pd.read_csv(
        f"data/{company}_financials.csv",
        index_col=0
    )

    try:

        revenue = df.loc["Total Revenue"].dropna()
        net_income = df.loc["Net Income"].dropna()
        ebitda = df.loc["EBITDA"].dropna()

        beginning_revenue = revenue.iloc[-1]
        ending_revenue = revenue.iloc[0]

        years = len(revenue) - 1

        cagr = (
            (
                ending_revenue /
                beginning_revenue
            ) ** (1 / years) - 1
        ) * 100

        latest_revenue = revenue.iloc[0]
        latest_income = net_income.iloc[0]
        latest_ebitda = ebitda.iloc[0]

        net_margin = (
            latest_income /
            latest_revenue
        ) * 100

        ebitda_margin = (
            latest_ebitda /
            latest_revenue
        ) * 100

        kpis.append({
            "Company": company,
            "Revenue CAGR %": round(cagr, 2),
            "Net Margin %": round(net_margin, 2),
            "EBITDA Margin %": round(ebitda_margin, 2)
        })

    except Exception as e:

        print(
            f"Error processing {company}: {e}"
        )

kpi_df = pd.DataFrame(kpis)

kpi_df.to_excel(
    "data/master_kpis.xlsx",
    index=False
)

print(kpi_df)

print(
    "\nmaster_kpis.xlsx created!"
)