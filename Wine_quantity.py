# Wine dataset analysis

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_wine

# Load dataset
wine = load_wine()

# Convert to DataFrame
qua = pd.DataFrame(wine.data, columns=wine.feature_names)

# -----------------------------
# Bar plot
# -----------------------------
sns.barplot(x="alcohol", y="proline", data=qua)
plt.title("Alcohol vs Proline")
plt.show()

# -----------------------------
# Histogram
# -----------------------------
sns.histplot(qua["proline"], kde=True)
plt.title("Proline Distribution")
plt.xlabel("Proline")
plt.ylabel("Count")
plt.show()

# -----------------------------
# Correlation heatmap
# -----------------------------
corr = qua.corr()

sns.heatmap(corr, annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.show()
