import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create simple dataset
data = {
    "Study Hours": [2, 3, 4, 5, 6, 7, 8],
    "Sleep Hours": [7, 6, 6, 5, 5, 4, 4],
    "Screen Time": [5, 4, 3, 3, 2, 2, 1],
    "Marks": [50, 55, 65, 70, 80, 85, 90]
}

df = pd.DataFrame(data)

# Calculate correlation
corr = df.corr()

# Plot heatmap
sns.heatmap(corr, annot=True)

plt.title("Correlation Heatmap")
plt.show()