import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
tips=sns.load_dataset("tips")
sns.scatterplot(data=tips,x="total_bill",y="tip",hue="sex")
plt.title("Bill vs Tip by Gender")
plt.show()
sns.barplot(x="sex",y="tip",hue="sex",data=tips)
plt.title("Average Tip by Gender")
plt.show()
sns.histplot(tips["tip"],kde=True)
plt.title("tips distribution")
plt.show()
corr=tips.corr(numeric_only=True)
sns.heatmap(corr,annot=True,cmap="Blues")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()