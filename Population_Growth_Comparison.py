import matplotlib.pyplot as plt

# -----------------------------
# Data
# -----------------------------
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

population_cityA = [2.5, 2.7, 2.9, 3.1, 3.4, 3.7, 4.0, 4.3]
population_cityB = [1.8, 1.9, 2.1, 2.3, 2.6, 2.9, 3.1, 3.4]
population_cityC = [3.0, 3.1, 3.2, 3.4, 3.6, 3.8, 4.1, 4.5]

# -----------------------------
# Multi-line Plot
# -----------------------------
plt.figure(figsize=(10,6))

plt.plot(years, population_cityA, marker="o", label="City A")
plt.plot(years, population_cityB, marker="s", label="City B")
plt.plot(years, population_cityC, marker="^", label="City C")

# Labels and Title
plt.title("Population Growth Comparison (2015–2022)")
plt.xlabel("Year")
plt.ylabel("Population (Millions)")

# Grid and Legend
plt.grid(True)
plt.legend()

plt.show()