# concepts: list, dictionary, loop, if-else

students = [
    {"name" : "Rohit", "marks" : 90},
    {"name" : "Aman", "marks" : 65},
    {"name" : "Priya", "marks" : 78},
    {"name" : "Riya", "marks" : 45},
    {"name" : "Siya", "marks" : 88}
]

for student in students:
    if student["marks"] >= 50:
        print(student["name"], "has passed the exam")
    else:
        print(student["name"], "has failed the exam")

for student in students:
    if student["marks"] >= 90:
        print(student["name"], "scored A grade")
    elif student["marks"] >= 75:
        print(student["name"], "scored B grade")
    elif student["marks"] >= 50:
        print(student["name"], "scored C grade")
    else:
        print(student["name"], "scored D grade")

count = 0

for student in students:
    if student["marks"] >= 75:
        count += 1

print("Number of students who scored above 75: ", count)

toppers = []
for student in students:
    if student["marks"] >= 75:
        toppers.append(student)

print("Toppers :",toppers)
