import pandas as pd
import os

raw_path = "Data/Raw"
processed_path = "Data/Processed"

os.makedirs(processed_path, exist_ok=True)

print("Starting Data Cleaning...")

# ----------------------------
# NAV HISTORY
# ----------------------------

nav = pd.read_csv(f"{raw_path}/02_nav_history.csv")

if "date" in nav.columns:
    nav["date"] = pd.to_datetime(nav["date"], errors="coerce")

sort_cols = []

if "amfi_code" in nav.columns:
    sort_cols.append("amfi_code")

if "date" in nav.columns:
    sort_cols.append("date")

if len(sort_cols) > 0:
    nav = nav.sort_values(sort_cols)

nav = nav.drop_duplicates()

if "nav" in nav.columns:
    nav = nav[nav["nav"] > 0]

    if "amfi_code" in nav.columns:
        nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

nav.to_csv(
    f"{processed_path}/02_nav_history_clean.csv",
    index=False
)

print("NAV History Cleaned")


# ----------------------------
# INVESTOR TRANSACTIONS
# ----------------------------

txn = pd.read_csv(
    f"{raw_path}/08_investor_transactions.csv"
)

# Fix all date columns automatically

for col in txn.columns:

    if "date" in col.lower():

        txn[col] = pd.to_datetime(
            txn[col],
            errors="coerce"
        )

# Standardize transaction type automatically

for col in txn.columns:

    if "transaction" in col.lower() and "type" in col.lower():

        txn[col] = (
            txn[col]
            .astype(str)
            .str.strip()
            .str.title()
        )

# Validate numeric columns

for col in txn.columns:

    if "amount" in col.lower():

        txn[col] = pd.to_numeric(
            txn[col],
            errors="coerce"
        )

        txn = txn[txn[col] > 0]

txn = txn.drop_duplicates()

txn.to_csv(
    f"{processed_path}/08_investor_transactions_clean.csv",
    index=False
)

print("Investor Transactions Cleaned")


# ----------------------------
# SCHEME PERFORMANCE
# ----------------------------

perf = pd.read_csv(
    f"{raw_path}/07_scheme_performance.csv"
)

for col in perf.columns:

    if "return" in col.lower():

        perf[col] = pd.to_numeric(
            perf[col],
            errors="coerce"
        )

if "expense_ratio" in perf.columns:

    perf["expense_ratio_flag"] = (
        (perf["expense_ratio"] < 0.1)
        |
        (perf["expense_ratio"] > 2.5)
    )

perf = perf.drop_duplicates()

perf.to_csv(
    f"{processed_path}/07_scheme_performance_clean.csv",
    index=False
)

print("Scheme Performance Cleaned")

print("Day 2 Cleaning Completed Successfully")