import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/creditcard.csv")

# ---------------- BASIC ANALYSIS ----------------

print("Total Transactions:", len(df))

fraud_count = df["Class"].sum()
print("Total Fraud Transactions:", fraud_count)

fraud_percent = (fraud_count / len(df)) * 100
print("Fraud Percentage:", round(fraud_percent, 4), "%")

print("\nAverage Transaction Amount:")
print(df["Amount"].mean())

print("\nLargest Transaction:")
print(df["Amount"].max())

# ---------------- FRAUD VS NORMAL ----------------

fraud = df[df["Class"] == 1]
normal = df[df["Class"] == 0]

print("\nAverage Fraud Transaction Amount:")
print(fraud["Amount"].mean())

print("\nAverage Normal Transaction Amount:")
print(normal["Amount"].mean())

# ---------------- RISK SCORING ----------------

def risk_level(amount):
    if amount > 2000:
        return "High Risk"
    elif amount > 500:
        return "Medium Risk"
    else:
        return "Low Risk"

df["Risk_Level"] = df["Amount"].apply(risk_level)

print("\nRisk Level Counts:")
print(df["Risk_Level"].value_counts())

# ---------------- VISUALIZATIONS ----------------

# Fraud vs Normal
class_counts = df["Class"].value_counts()

plt.bar(["Normal", "Fraud"], class_counts)
plt.title("Fraud vs Normal Transactions")
plt.xlabel("Transaction Type")
plt.ylabel("Count")
plt.show()

# Transaction Amount Distribution
plt.hist(df["Amount"], bins=50)
plt.title("Transaction Amount Distribution")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.show()

# Fraud Transaction Amounts
plt.hist(fraud["Amount"], bins=30)
plt.title("Fraud Transaction Amounts")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.show()

# Risk Level Distribution
risk_counts = df["Risk_Level"].value_counts()

plt.bar(risk_counts.index, risk_counts.values)
plt.title("Risk Level Distribution")
plt.xlabel("Risk Level")
plt.ylabel("Count")
plt.show()

# Fraud Over Time
plt.scatter(fraud["Time"], fraud["Amount"])
plt.title("Fraud Transactions Over Time")
plt.xlabel("Time")
plt.ylabel("Amount")
plt.show()