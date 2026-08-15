# Student Analyzer
def addStudent(name, marks):
    students.append({"name": name, "marks": marks})

def findTopper(students):
    topper = students[0]

    for student in students:
        if student["marks"] > topper["marks"]:
            topper = student
    
    return topper["name"]

def calculateAverage(students):
    total = 0

    for student in students:
        total += student["marks"]
    
    avg = total / len(students)
    return avg

def weakStudents(students):
    weakstudents = []

    for student in students:
        if student["marks"] < 40:
            weakstudents.append(student["name"])

    return weakstudents

students = []

addStudent("Rohit", 90)
addStudent("Kabir", 80)
addStudent("Dev", 70)
addStudent("Rudrani", 35)
addStudent("Ojas", 30)

print("--- Student Analyzer ---")
print("Total Students:", len(students))
print("Topper:", findTopper(students))
print("Average Marks:", calculateAverage(students))
print("Weak Students:", weakStudents(students))
