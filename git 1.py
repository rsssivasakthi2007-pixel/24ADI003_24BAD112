print("SIVASAKTHI 24BAD112")
import pandas as pd, matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\priya\Downloads\archive (8).zip", encoding="latin1").dropna()
df = df[(df.Quantity > 0) & (df.UnitPrice > 0)]
df["Revenue"] = df.Quantity * df.UnitPrice
df["Month"] = pd.to_datetime(df.InvoiceDate).dt.to_period("M")
ms = df.groupby("Month").Revenue.sum(); print(ms.head())
fig, ax = plt.subplots(1,2,figsize=(12,5))
ms.plot(ax=ax[0], marker="o", title="Monthly Sales (Line)")
ms.plot(ax=ax[1], kind="bar", color="skyblue", title="Monthly Sales (Bar)")
for a in ax: a.set(xlabel="Month", ylabel="Revenue")
plt.tight_layout(); plt.show()
print(df.groupby("Description").Revenue.sum().nlargest(5))
