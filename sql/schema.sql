CREATE TABLE dim_fund (
fund_id INTEGER PRIMARY KEY,
amfi_code INTEGER,
fund_name TEXT,
fund_house TEXT,
category TEXT
);

CREATE TABLE dim_date (
date_id INTEGER PRIMARY KEY,
date DATE
);

CREATE TABLE fact_nav (
nav_id INTEGER PRIMARY KEY,
amfi_code INTEGER,
date DATE,
nav REAL
);

CREATE TABLE fact_transactions (
txn_id INTEGER PRIMARY KEY,
transaction_type TEXT,
amount REAL
);

CREATE TABLE fact_performance (
perf_id INTEGER PRIMARY KEY,
amfi_code INTEGER,
return_1y REAL,
return_3y REAL,
return_5y REAL,
expense_ratio REAL
);

CREATE TABLE fact_aum (
aum_id INTEGER PRIMARY KEY,
fund_house TEXT,
aum REAL
);