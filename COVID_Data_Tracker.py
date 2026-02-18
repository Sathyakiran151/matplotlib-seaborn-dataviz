'''🔹 6️⃣ COVID Data Tracker (Simplified)

Goal: Analyze COVID cases for multiple days.
Hint:

Use an array of daily new cases.

Find total cases, average daily cases, and days with above-average case'''
import numpy as np
case=np.array([12,54,65,86,56,32,96,98,168,74,55,14])# 12 day cases
average=np.mean(case,dtype="int")
print("The Average daily cases are :",average)
print(f"\nThe Highest cases in a day : {np.max(case)} ({np.argmax(case+1)})day")
print(f"The Lowest cases in a day : {np.min(case)} ({np.argmin(case)+1})day")

total=np.sum(case)
print("\nThe Total cases in 12 days are :",total)
above=np.where(case>average)
print("\nThe Above Average cases are :")
for i in above[0]:
    print(f"IN {i+1} day {case[i]} cases  ")


