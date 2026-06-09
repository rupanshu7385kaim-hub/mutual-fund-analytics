-- Top 5 Funds

SELECT * FROM fund_master LIMIT 5;

-- Average NAV

SELECT amfi_code,
AVG(nav)
FROM nav_history
GROUP BY amfi_code;

-- Expense Ratio Less Than 1

SELECT *
FROM performance
WHERE expense_ratio < 1;

-- Highest 5 Year Return

SELECT *
FROM performance
ORDER BY return_5y DESC
LIMIT 5;

-- Total Transactions

SELECT COUNT(*)
FROM transactions;

-- Total Funds

SELECT COUNT(*)
FROM fund_master;

-- Average Expense Ratio

SELECT AVG(expense_ratio)
FROM performance;

-- Maximum NAV

SELECT MAX(nav)
FROM nav_history;

-- Minimum NAV

SELECT MIN(nav)
FROM nav_history;

-- Top NAV Schemes

SELECT amfi_code,
AVG(nav)
FROM nav_history
GROUP BY amfi_code
ORDER BY AVG(nav) DESC
LIMIT 5;