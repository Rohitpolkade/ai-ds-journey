"""Student Performance Analyzer"""
import numpy as np

marks = np.array([85, 90, 80, 70, 60])

print("---Student Performance Report---")
print()
print(f"Highest Marks :{np.max(marks)}")
print(f"Lowest Marks :{np.min(marks)}")
print(f"Average Marks :{np.mean(marks)}")
print(f"Total Marks :{np.sum(marks)}")
print()

# print students marks who scored above avg marks!
print("Students Above Average:")
avg = np.mean(marks)
above_avg = marks[marks > avg]
print(above_avg)

# count number of students who scored more than 80
print()
count = 0
for i in marks[marks > 80]:
    count += 1
print(f"Students above 80: {count}")
print()

# Adding 5 grace marks
marks = marks + 5

print("Marks After Grace:")
print(marks)
