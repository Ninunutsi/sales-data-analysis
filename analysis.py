import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/sales.csv')

df["date"] = pd.to_datetime(df["date"])
print(df.head())

revenue = df["revenue"] = df["quantity"] * df["price"]
# print(df.head())

best_products = (df.groupby("product")["quantity"].sum().sort_values(ascending=False).reset_index())

product_revenue = (df.groupby("product")["revenue"].sum().sort_values(ascending=False).reset_index())

df["month"] = df["date"].dt.to_period("M")
month_sales = df.groupby("month")["revenue"].sum().reset_index()

month_sales.plot(kind="line")
plt.title("Monthly sales by revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

product_revenue.sort_values(by="revenue").plot(x="product", y="revenue",kind="barh")
plt.title("Revenue by Product")
plt.xlabel("Revenue")
plt.ylabel("product")
plt.tight_layout()
plt.show()

