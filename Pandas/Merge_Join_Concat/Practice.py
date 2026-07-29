import pandas as pd

print("=" * 50)
print("Student Result Combiner")
print("=" * 50)

students = pd.DataFrame({
    "IDs" : [1, 2, 3],
    "Names" : ["Rohit", "Dev", "kabir"]
})

marks = pd.DataFrame({
    "IDs" : [1, 2, 3],
    "Marks" : [90, 91, 92]
})

result = pd.merge(students, marks)
print("\nMerged DataFrame:")
print(result)

dept = pd.DataFrame({
    "Department": ["AI", "CSE", "IT"]
}, index=[0, 1, 2])

info = result.join(dept)
print("\nJoined DataFrame:")
print(info)

roll_no = pd.DataFrame({
    "Roll_No" : [17, 21, 25]
})

details = pd.concat([info, roll_no], axis = 1)
print("\nConcatenated DataFrame:")
print(details)