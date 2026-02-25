import matplotlib.pyplot as plt
import numpy as np
fig1=plt.figure(figsize=(12,8))

x=["Telugu","Hindi","English","maths","science"]
st1=[70,83,85,90,75]
st2=[80,89,85,90,75]
st3=[60,93,95,50,75]
st4=[70,93,75,30,55]
st5=[60,53,65,60,73]

avg_marks=[np.mean(st1),np.mean(st2),np.mean(st3),np.mean(st4),np.mean(st5)]
Student=["Student1","Student2","Student3","Student4","Student5"]

plt.subplot(2,2,1)
plt.bar(x,st1,color="red")
plt.title("The percentage of an Student1")
plt.xlabel("The Student Name")
plt.ylabel("The Percentage  ")

plt.subplot(2,2,2)
plt.bar(x,st2,color="green")
plt.title("The percentage of an Student2")
plt.xlabel("The Student Name")
plt.ylabel("The Percentage  ")

plt.subplot(2,2,3)
plt.bar(x,st3,color="blue")
plt.title("The percentage of an Student3")
plt.xlabel("The Student Name")
plt.ylabel("The Percentage  ")


plt.subplot(2,2,4)
plt.bar(x,st4,color="purple")
plt.title("The percentage of an Student4")
plt.xlabel("The Student Name")
plt.ylabel("The Percentage  ")
plt.tight_layout()
plt.show()



plt.plot(Student,avg_marks,marker="o")
plt.title("The Average marks of student in subjects ")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()