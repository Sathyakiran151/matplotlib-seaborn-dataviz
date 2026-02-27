import matplotlib.pyplot as plt
import numpy as np
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
temperature=[30, 32, 35, 31, 29, 28, 33]
avg_temp = np.mean(temperature)
plt.plot(days,temperature,marker="o",label="Daily temperature")
plt.axhline(avg_temp,linestyle="--",label="Average Temp")
max_temp = max(temperature)
min_temp = min(temperature)
plt.scatter(days,temperature)
plt.scatter(days[temperature.index(max_temp)],max_temp,color="red",label="max Temp",s=150)
plt.scatter(days[temperature.index(min_temp)],min_temp,color="green",label="min Temp",s=150)

plt.xlabel("Days")
plt.ylabel("Temperature C ")
plt.title("Weekly Temperature Analysis")
plt.legend()

plt.show()