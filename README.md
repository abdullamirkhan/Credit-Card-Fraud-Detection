# Credit Card Fraud Detection Analysis

## Overview
This project analyzes real-world credit card transaction data to identify fraudulent behavior and high-risk transaction patterns using Python and SQL.

The dataset contains anonymized transaction features and transaction amounts used to distinguish fraudulent transactions from legitimate ones.

---

## Tools & Technologies
- Python
- Pandas
- Matplotlib
- SQL

---

## Features

### Fraud Analysis
- Identified fraudulent transactions
- Calculated fraud percentage
- Compared fraud vs normal transaction behavior

### Risk Scoring
Transactions were classified into:
- Low Risk
- Medium Risk
- High Risk

based on transaction amount.

### Data Visualization
Created visualizations including:
- Fraud vs Normal transaction counts
- Transaction amount distribution
- Fraud transaction distribution
- Risk level distribution
- Fraud transactions over time

### SQL Analysis
Used SQL queries to:
- Count fraudulent transactions
- Calculate fraud percentage
- Identify high-value transactions
- Analyze fraud transaction amounts

---

## How to Run

### Install Libraries
```bash
pip3 install -r requirements.txt
```

### Run Project
```bash
python3 analysis.py
```

---

## Project Structure
```text
credit-card-fraud-analysis/
├── analysis.py
├── queries.sql
├── README.md
├── requirements.txt
└── data/
    └── creditcard.csv
```

---

## Future Improvements
- Add machine learning fraud prediction model
- Build interactive dashboard
- Implement anomaly detection
- Add real-time fraud monitoring

---

## Author
Amir Khan