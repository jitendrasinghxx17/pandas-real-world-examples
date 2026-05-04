
---

# `pandas_scenarios.py` (MAIN CODE)

```python
import pandas as pd
import numpy as np

# -------------------------------
# Scenario 1: Customer Spending
# -------------------------------
print("\n--- Scenario 1: Customer Spending ---")

customers = pd.DataFrame({
    "customer_id": [1, 2, 3],
    "name": ["A", "B", "C"]
})

orders = pd.DataFrame({
    "order_id": [101, 102],
    "customer_id": [1, 2],
    "amount": [100, 200]
})

df = pd.merge(customers, orders, on="customer_id", how="left")

result = df.groupby("customer_id")["amount"].sum().fillna(0)
print(result)


# -------------------------------
# Scenario 2: Handling Missing Data
# -------------------------------
print("\n--- Scenario 2: Missing Data ---")

df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "salary": [50000, None, 60000]
})

df["salary"].fillna(df["salary"].mean(), inplace=True)
print(df)


# -------------------------------
# Scenario 3: Remove Duplicates
# -------------------------------
print("\n--- Scenario 3: Duplicates ---")

df = pd.DataFrame({
    "txn_id": [1, 2, 2, 3],
    "amount": [100, 200, 200, 300]
})

df = df.drop_duplicates(subset=["txn_id"])
print(df)


# -------------------------------
# Scenario 4: Feature Engineering
# -------------------------------
print("\n--- Scenario 4: Feature Engineering ---")

df = pd.DataFrame({
    "marks": [40, 75, 30, 90]
})

df["result"] = np.where(df["marks"] >= 50, "Pass", "Fail")
print(df)


# -------------------------------
# Scenario 5: Combine Monthly Data
# -------------------------------
print("\n--- Scenario 5: Concat ---")

jan = pd.DataFrame({"sales": [100, 200]})
feb = pd.DataFrame({"sales": [300, 400]})

df = pd.concat([jan, feb])
print(df)


# -------------------------------
# Scenario 6: Customers with No Orders
# -------------------------------
print("\n--- Scenario 6: No Orders ---")

df = pd.merge(customers, orders, on="customer_id", how="left")
no_orders = df[df["order_id"].isnull()]
print(no_orders)


# -------------------------------
# Scenario 7: Pivot Table
# -------------------------------
print("\n--- Scenario 7: Pivot Table ---")

df = pd.DataFrame({
    "region": ["North", "North", "South"],
    "product": ["A", "B", "A"],
    "sales": [100, 200, 300]
})

pivot = pd.pivot_table(df, values="sales", index="region", columns="product", aggfunc="sum")
print(pivot)


# -------------------------------
# Scenario 8: Chunk Processing
# -------------------------------
print("\n--- Scenario 8: Chunk Processing ---")

# Simulating large file
large_df = pd.DataFrame({
    "sales": np.random.randint(1, 100, size=100000)
})

large_df.to_csv("large_file.csv", index=False)

total = 0
for chunk in pd.read_csv("large_file.csv", chunksize=20000):
    total += chunk["sales"].sum()

print("Total Sales:", total)
