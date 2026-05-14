CREATE TABLE creditcard_transactions (
    Time FLOAT,
    Amount FLOAT,
    Class INT
);

-- Total fraud transactions
SELECT COUNT(*)
FROM creditcard_transactions
WHERE Class = 1;

-- Average transaction amount
SELECT AVG(Amount)
FROM creditcard_transactions;

-- Highest transactions
SELECT *
FROM creditcard_transactions
ORDER BY Amount DESC
LIMIT 10;

-- Average fraud transaction amount
SELECT AVG(Amount)
FROM creditcard_transactions
WHERE Class = 1;

-- Fraud percentage
SELECT 
    (SUM(Class) * 100.0 / COUNT(*)) AS fraud_percentage
FROM creditcard_transactions;