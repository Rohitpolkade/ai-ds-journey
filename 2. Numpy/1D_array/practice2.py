'''Student Data Generator'''
import numpy as np 

marks = np.random.randint(40, 100, 20)
print("Marks:")
print(marks)

attendence = np.random.randint(60, 100, 20)
print("\nAttendence:")
print(attendence)

print(f"\nHighest Mark: {np.max(marks)}")
print(f"Lowest Mark: {np.min(marks)}")
print(f"Avg Marks: {np.mean(marks)}")
print(f"Avg Attendence: {np.mean(attendence)}")

print()
identityMatrix = np.eye(5)
print("Identity Matrix:")
print(identityMatrix)

print()
numbArr = np.full((3, 3), 100)
print("Full Matrix:")
print(numbArr)