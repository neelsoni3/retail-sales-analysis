import pandas as pd
import numpy as np

df = pd.read_csv("E:/retail-sales-analysis/data/Dataset.csv")

print("Rows in CSV:", len(df))
print("Years in data:", sorted(df["YEAR"].unique().tolist()))
print()

df = df.dropna(subset=["SUPPLIER", "MONTH", "ITEM TYPE", "RETAIL SALES"])
df["MONTH"] = df["MONTH"].astype(int)
df["RETAIL SALES"] = pd.to_numeric(df["RETAIL SALES"], errors="coerce").fillna(0)

suppliers  = sorted(df["SUPPLIER"].unique())
item_types = sorted(df["ITEM TYPE"].unique())
months     = sorted(df["MONTH"].unique().tolist())

print(f"Suppliers:  {len(suppliers)}")
print(f"Item types: {len(item_types)}")
print(f"Months:     {months}")
print()

sales = np.zeros((len(suppliers), len(months), len(item_types)))

supplier_idx = {name: i for i, name in enumerate(suppliers)}
month_idx    = {month: i for i, month in enumerate(months)}
item_idx     = {name: i for i, name in enumerate(item_types)}

grouped = df.groupby(["SUPPLIER", "MONTH", "ITEM TYPE"])["RETAIL SALES"].sum()

for (supplier, month, item_type), total in grouped.items():
    sales[supplier_idx[supplier], month_idx[month], item_idx[item_type]] = total

print("Sales array shape:", sales.shape)
print("Total revenue:    ", round(sales.sum(), 2))
print()

supplier_totals  = sales.sum(axis=(1, 2))
month_totals     = sales.sum(axis=(0, 2))
item_type_totals = sales.sum(axis=(0, 1))

print("Top 10 suppliers by revenue:")
for i in np.argsort(supplier_totals)[::-1][:10]:
    print(f"  {suppliers[i]:<35} {supplier_totals[i]:14.2f}")
print()

print("Total revenue per month:")
for i, total in enumerate(month_totals):
    month_name = pd.Timestamp(2024, months[i], 1).strftime("%B")
    print(f"  {month_name:<12} {total:14.2f}")
print()

print("Total revenue per item type:")
for name, total in zip(item_types, item_type_totals):
    print(f"  {name:<20} {total:14.2f}")
print()

best_supplier  = suppliers[np.argmax(supplier_totals)]
best_item_type = item_types[np.argmax(item_type_totals)]
best_month     = pd.Timestamp(2024, months[np.argmax(month_totals)], 1).strftime("%B")

print("Best of each category:")
print(f"  Supplier  -> {best_supplier}")
print(f"  Item type -> {best_item_type}")
print(f"  Month     -> {best_month}")
print()

print("Overall statistics (all cells, including empty ones):")
print(f"  mean   = {sales.mean():.2f}")
print(f"  median = {np.median(sales):.2f}")
print(f"  std    = {sales.std():.2f}")
print(f"  min    = {sales.min():.2f}")
print(f"  max    = {sales.max():.2f}")
print()

non_zero = sales[sales > 0]
print("Statistics (non-zero cells only):")
print(f"  count  = {len(non_zero)}")
print(f"  mean   = {non_zero.mean():.2f}")
print(f"  median = {np.median(non_zero):.2f}")
print(f"  std    = {non_zero.std():.2f}")
print(f"  min    = {non_zero.min():.2f}")
print(f"  max    = {non_zero.max():.2f}")
print()

avg_month = month_totals.mean()
print(f"Months with revenue above average ({avg_month:.2f}):")
for i, total in enumerate(month_totals):
    if total > avg_month:
        month_name = pd.Timestamp(2024, months[i], 1).strftime("%B")
        print(f"  {month_name:<12} ({total:.2f})")
print()

threshold = np.percentile(non_zero, 99)
print(f"Top 1% of real sales (above {threshold:.2f}):")
for s, m, p in zip(*np.where(sales > threshold)):
    print(f"  {suppliers[s]:<35} {months[m]:>2}  {item_types[p]:<15} {sales[s, m, p]:12.2f}")

print("\nAnalysis complete.")