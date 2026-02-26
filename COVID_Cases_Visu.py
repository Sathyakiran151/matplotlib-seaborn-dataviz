import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Day": [1,2,3,4,5,6,7],
    "Cases": [100, 150, 200, 250, 300, 280, 260],
    "Recovered": [20, 40, 60, 100, 150, 180, 210]
}

df = pd.DataFrame(data)

plt.plot(df["Day"], df["Cases"], label="Cases")
plt.plot(df["Day"], df["Recovered"], label="Recovered")

plt.xlabel("Day")
plt.ylabel("Count")
plt.title("COVID Trend")
plt.legend()
plt.show()