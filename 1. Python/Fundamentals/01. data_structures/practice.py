# Concepts: list, dictionary, lambda, max, sum, list comprehension

students = [
    {"name" : "Rohit", "marks" : 90},
    {"name" : "Kabir", "marks" : 70},
    {"name" : "Dev", "marks" : 80}
]

# find the topper
topper = max(students, key = lambda x: x["marks"])
print(topper["name"])

# calculate avg marks
avg = sum(student["marks"] for student in students)/ len(students)
print(avg)

# find students who scored above 75
aboveAvg = [student["name"] for student in students if student["marks"] > 75]

for name in aboveAvg:
    print(name)

# add a new student
students.append({"name" : "C", "marks" : 95})

# new topper
topper = max(students, key = lambda x: x["marks"])
print(topper["name"])