import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set()
# Sample data
data = {
    "Height": [150, 155, 160, 165, 170, 175, 180],
    "Weight": [50, 55, 60, 65, 70, 75, 80]
}

df = pd.DataFrame(data)

# Scatterplot
sns.scatterplot(x="Height", y="Weight", data=df)
sns.regplot(x="Height", y="Weight", data=df)

plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.show()