print("SIVASAKTHI 24BAD112")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\Users\priya\Downloads\archive (12).zip")
print(df.head())
print(df.info())
print(df.isnull().sum())
plt.scatter(df["area"], df["price"])
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs Price")
plt.show()
numeric_df = df.select_dtypes(include="number")
sns.heatmap(numeric_df.corr(), annot=True)
plt.title("Feature Correlation Heatmap")
plt.show()
