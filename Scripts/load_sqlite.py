import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

tables = {

    "fund_master":
    "Data/Raw/01_fund_master.csv",

    "nav_history":
    "Data/Processed/02_nav_history_clean.csv",

    "transactions":
    "Data/Processed/08_investor_transactions_clean.csv",

    "performance":
    "Data/Processed/07_scheme_performance_clean.csv"

}

for table, file in tables.items():

    df = pd.read_csv(file)

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(table, "loaded")

print("SQLite Database Created Successfully")