import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("assets", exist_ok=True)

np.random.seed(42)
n = 1200

products = np.random.choice(["Chair", "Desk", "Laptop", "Monitor", "Phone", "Printer", "Tablet"], n)
payment_methods = np.random.choice(["Cash", "Credit Card", "Debit Card", "Gift Card", "Online"], n)
statuses = np.random.choice(["Cancelled", "Delivered", "Pending", "Returned", "Shipped"], n)
coupons = np.random.choice([None, "SAVE10", "FREESHIP", "WINTER15"], n, p=[0.3, 0.3, 0.2, 0.2])
sources = np.random.choice(["Instagram", "Facebook", "Google", "Referral", "Email"], n)

df = pd.DataFrame({
    "OrderID": [f"ORD{200000 + i}" for i in range(n)],
    "Date": pd.date_range("2023-01-01", periods=n, freq="h")[:n],
    "CustomerID": [f"C{np.random.randint(10000, 90000)}" for _ in range(n)],
    "Product": products,
    "Quantity": np.random.randint(1, 6, n),
    "UnitPrice": np.round(np.random.uniform(10, 700, n), 2),
    "PaymentMethod": payment_methods,
    "OrderStatus": statuses,
    "CouponCode": coupons,
    "ReferralSource": sources,
})
df["TotalPrice"] = np.round(df["Quantity"] * df["UnitPrice"] * np.random.uniform(0.9, 1.1, n), 2)

sns.set_style("whitegrid")
plt.rcParams.update({"figure.dpi": 120, "savefig.dpi": 150, "savefig.bbox": "tight"})

fix, ax = plt.subplots(figsize=(10, 5))
df["Product"].value_counts().plot(kind="bar", ax=ax, color="#4A72B0")
ax.set_title("Order Count by Product", fontsize=14, fontweight="bold")
ax.set_xlabel("Product")
ax.set_ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("assets/product_counts.png")
plt.close()

fig, ax = plt.subplots(figsize=(10, 5))
df.groupby("Product")["TotalPrice"].sum().sort_values().plot(kind="barh", ax=ax, color="#4A72B0")
ax.set_title("Total Revenue by Product", fontsize=14, fontweight="bold")
ax.set_xlabel("Revenue ($)")
ax.set_ylabel("Product")
plt.tight_layout()
plt.savefig("assets/revenue_by_product.png")
plt.close()

fig, ax = plt.subplots(figsize=(8, 8))
df["PaymentMethod"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax, colors=sns.color_palette("Set2"))
ax.set_title("Payment Method Distribution", fontsize=14, fontweight="bold")
ax.set_ylabel("")
plt.tight_layout()
plt.savefig("assets/payment_methods.png")
plt.close()

fig, ax = plt.subplots(figsize=(10, 5))
df["OrderStatus"].value_counts().plot(kind="bar", ax=ax, color="#4A72B0")
ax.set_title("Orders by Status", fontsize=14, fontweight="bold")
ax.set_xlabel("Order Status")
ax.set_ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("assets/order_status.png")
plt.close()

fig, ax = plt.subplots(figsize=(10, 5))
df["Quantity"].plot(kind="hist", bins=5, ax=ax, color="#4A72B0", edgecolor="white")
ax.set_title("Quantity per Order", fontsize=14, fontweight="bold")
ax.set_xlabel("Quantity")
ax.set_ylabel("Frequency")
plt.tight_layout()
plt.savefig("assets/quantity_distribution.png")
plt.close()

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df[["Quantity", "UnitPrice", "TotalPrice"]].corr(), annot=True, cmap="coolwarm", center=0, ax=ax)
ax.set_title("Correlation Matrix", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("assets/correlation_matrix.png")
plt.close()

print("All screenshots saved to assets/")
