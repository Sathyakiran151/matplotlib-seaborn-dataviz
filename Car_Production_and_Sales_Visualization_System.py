import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# DATA
# -----------------------------
car = ["Audi","Bmw","MG","Tata","Defender"]
sales = [200,300,500,1000,400]

monthly = ["Jan","Feb","Mar","Apr","May","Jun",
           "Jul","Aug","Sep","Oct","Nov","Dec"]

# 12 values for 12 months
man_car1=[344,390,338,853,383,596,343,557,755,787,654,500]
man_car2=[644,890,438,853,383,596,343,757,515,187,154,450]
man_car3=[544,890,638,853,383,596,343,557,755,787,354,600]
man_car5=[222,590,438,653,683,896,943,557,755,787,654,520]

# -----------------------------
# CREATE DASHBOARD
# -----------------------------
plt.figure(figsize=(12,8))

# 1️⃣ Bar chart
plt.subplot(2,2,1)
plt.bar(car, sales, color="blue")
plt.title("Car Sales (Bar Chart)")
plt.xlabel("Cars")
plt.ylabel("Sales")

# 2️⃣ Line chart
plt.subplot(2,2,2)
plt.plot(car, sales, marker='o')
plt.title("Car Sales Trend")
plt.xlabel("Cars")
plt.ylabel("Sales")

# 3️⃣ Manufacturing trend
plt.subplot(2,2,3)
plt.plot(monthly, man_car1, marker='o')
plt.title("Manufacturing - Car 1")
plt.xlabel("Months")
plt.ylabel("Production")
plt.xticks(rotation=45)

# 4️⃣ Compare multiple cars
plt.subplot(2,2,4)
plt.plot(monthly, man_car1, label="Car1")
plt.plot(monthly, man_car2, label="Car2")
plt.plot(monthly, man_car3, label="Car3")
plt.plot(monthly, man_car5, label="Car5")
plt.title("Monthly Manufacturing Comparison")
plt.xlabel("Months")
plt.ylabel("Production")
plt.legend()
plt.xticks(rotation=45)

# -----------------------------
# SHOW ALL
# -----------------------------
plt.tight_layout()
plt.show()
plt.savefig("car_sales_dashboard.png")


