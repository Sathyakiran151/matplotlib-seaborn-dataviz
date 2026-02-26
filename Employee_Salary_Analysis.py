import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    "Employee": ["A","B","C","D","E","F","G","H"],
    "Department": ["IT","HR","IT","Finance","HR","Finance","IT","HR"],
    "Experience": [2,5,3,7,4,6,1,8],
    "Salary": [40000,50000,45000,70000,52000,68000,38000,75000]
}

df = pd.DataFrame(data)

# Boxplot - Salary by Department
sns.boxplot(x="Department", y="Salary", data=df)
plt.title("Salary Distribution by Department")
plt.show()

# Scatter plot - Experience vs Salary
sns.scatterplot(x="Experience", y="Salary", hue="Department", data=df)
plt.title("Experience vs Salary")
plt.show()