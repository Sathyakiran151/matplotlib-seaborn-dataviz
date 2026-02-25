import numpy as np
import matplotlib.pyplot as plt
subject=["telugu","hindi","English","science","Social"]
# marks in each exam 
exam1=[78,98,67,87,67]
exam2=[87,89,56,78,98]
exam3=[78,97,87,55,87]
# Combine all marks for histogram
all_marks = exam1 + exam2 + exam3

# Average marks per exam (performance trend)
avg_marks = [
    np.mean(exam1),
    np.mean(exam2),
    np.mean(exam3)
]

exams = ["Exam 1", "Exam 2", "Exam 3"]

# ==============================
# CREATE DASHBOARD
# ==============================

plt.figure(figsize=(12, 8))

plt.subplot(2,2,1)
plt.bar(subject,exam1,color="Blue")
plt.title("Marks per subject(Exam1)")
plt.xlabel("Subjects")
plt.ylabel("marks")
plt.xticks(rotation=20)

plt.subplot(2, 2, 2)
plt.pie(exam1, labels=subject, autopct="%1.1f%%")
plt.title("Subject Weightage")


plt.subplot(2, 2, 3)
plt.hist(all_marks, bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.subplot(2, 2, 4)
plt.plot(exams, avg_marks, marker='o')
plt.title("Performance Trend")
plt.xlabel("Exams")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.show()


