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

    try:

        income_df = pd.read_csv(
            f"data/{company}_financials.csv",
            index_col=0
        )

        balance_df = pd.read_csv(
            f"data/{company}_balance_sheet.csv",
            index_col=0
        )

        revenue = income_df.loc["Total Revenue"].dropna()
        net_income = income_df.loc["Net Income"].dropna()

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

        net_margin = (
            latest_income /
            latest_revenue
        ) * 100

        try:

            ebitda = income_df.loc["EBITDA"].dropna()

            latest_ebitda = ebitda.iloc[0]

            ebitda_margin = (
                latest_ebitda /
                latest_revenue
            ) * 100

        except:

            ebitda_margin = None

        equity = balance_df.loc[
            "Stockholders Equity"
        ].dropna()

        debt = balance_df.loc[
            "Total Debt"
        ].dropna()

        latest_equity = equity.iloc[0]
        latest_debt = debt.iloc[0]

        roe = (
            latest_income /
            latest_equity
        ) * 100

        debt_equity = (
            latest_debt /
            latest_equity
        )

        kpis.append({

            "Company": company,

            "Revenue CAGR %":
            round(cagr, 2),

            "Net Margin %":
            round(net_margin, 2),

            "EBITDA Margin %":
            round(ebitda_margin, 2)
            if ebitda_margin
            else None,

            "ROE %":
            round(roe, 2),

            "Debt/Equity":
            round(debt_equity, 2)

        })

    except Exception as e:

        print(
            f"Error processing {company}: {e}"
        )

kpi_df = pd.DataFrame(kpis)

kpi_df.to_excel(
    "data/master_kpis_v2.xlsx",
    index=False
)

print(kpi_df)

print(
    "\nmaster_kpis_v2.xlsx created!"
)