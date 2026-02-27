import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create simple sample data
experience = [1, 2, 3, 4, 5, 6, 7, 8]
salary = [15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]

# Create table
data = pd.DataFrame({
    "Experience": experience,
    "Salary": salary
})

# Plot scatter + regression line
sns.regplot(x="Experience", y="Salary", data=data)

# Title and labels
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")

# Show graph
plt.show()