import numpy as np

marks = np.random.randint(40, 101, size = 20)
attendance = np.random.randint(60, 101, size = 20)

print("=" * 50)
print("      STUDENT ANALYTICS DASHBOARD")
print("=" * 50)
print(f"\nMarks:\n{marks}")
print(f"\nAttendance:\n{attendance}")

print(f"\nHighest Marks : {np.max(marks)}")
print(f"Lowest Marks  : {np.min(marks)}")
print(f"Average Marks : {np.mean(marks):.2f}")
print(f"Total Marks   : {np.sum(marks)}")

above80 = marks[marks > 80]
print(f"\nStudent Above 80:\n{above80}")

below50 = marks[marks < 50]
print(f"\nStudent Below 50:\n{below50}")

# Reshape marks into a 4x5 matrix
new_marks = marks.reshape(4, 5)
print(f"\nMarks Matrix:")
print(new_marks)

print(f"\nFirst Row:{new_marks[0]}")
print(f"\nLast Column:{new_marks[:, 4]}")

flatten_marks = new_marks.flatten()
print(f"\nFlattened Array:\n{flatten_marks}")

print(f"\nMarks After Grace:\n{flatten_marks + 5}")

eligible_students = marks[ (marks >= 60) & (attendance >= 75)]
print(f"\nEligible Students:\n{eligible_students}")