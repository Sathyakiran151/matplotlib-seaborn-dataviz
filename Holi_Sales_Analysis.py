
# HOLI SALES ANALYSIS 


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create Dataset

data = {
    "Color": ["Red", "Blue", "Green", "Yellow", "Pink"],
    "Price_per_kg": [200, 180, 150, 170, 220],
    "Quantity_Sold_kg": [500, 450, 600, 550, 400]
}

df = pd.DataFrame(data)
sns.set()

# Calculate Revenue
df["Revenue"] = df["Price_per_kg"] * df["Quantity_Sold_kg"]

# 2. Creating Subplot Layout


plt.figure(figsize=(12,8))

# (1) Bar Chart - Price
plt.subplot(2,2,1)
plt.bar(df["Color"], df["Price_per_kg"])
plt.title("Price Comparison Of Colors")
plt.xlabel("Colors")
plt.ylabel("Price per kg")

# (2) Pie Chart - Revenue
plt.subplot(2,2,2)
plt.pie(df["Revenue"], labels=df["Color"], autopct="%1.1f%%")
plt.title("Revenue Distribution")

# (3) Correlation Heatmap
plt.subplot(2,2,3)
sns.heatmap(df[["Price_per_kg", "Quantity_Sold_kg", "Revenue"]].corr(),
            annot=True)
plt.title("Correlation Heatmap")

# (4) Line Plot - Quantity Sold
plt.subplot(2,2,4)
plt.plot(df["Color"], df["Quantity_Sold_kg"], marker="o")
plt.title("Sales Trend")
plt.xlabel("Colors")
plt.ylabel("Quantity Sold")

plt.tight_layout()
plt.show()