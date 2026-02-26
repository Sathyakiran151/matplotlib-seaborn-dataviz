import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Brand": ["A","B","C","D","E","F"],
    "RAM_GB": [4,6,8,12,6,8],
    "Storage_GB": [64,128,128,256,64,256],
    "Price": [15000,20000,25000,40000,18000,30000]
}

df = pd.DataFrame(data)

# Bubble scatter plot
plt.scatter(df["RAM_GB"], df["Price"], s=df["Storage_GB"]*2)
plt.xlabel("RAM (GB)")
plt.ylabel("Price")
plt.title("RAM vs Price (Bubble size = Storage)")
plt.show()

# Regression plot
sns.regplot(x="RAM_GB", y="Price", data=df)
plt.title("RAM vs Price Trend")
plt.show()