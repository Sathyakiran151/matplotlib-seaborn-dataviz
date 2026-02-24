import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
titanic=sns.load_dataset("titanic")

sns.countplot(x="sex",data=titanic)
plt.title("Survival count by gender")
plt.show()

sns.barplot(x="class",y="survived",data=titanic)
plt.title("Survival count by gender")
plt.show()



sns.histplot(titanic["age"])
plt.title(" Age distribution of passengers  ")
plt.show()

corr=titanic.corr(numeric_only=True)
sns.heatmap(corr,annot=True,cmap="Blues")
plt.title("Correlation Heatmap ")
plt.show()