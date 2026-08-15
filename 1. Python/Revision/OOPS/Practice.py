class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def showDetails(self):
        print(self.name, self.marks)
    
    def showGrade(self):
        if(self.marks >= 90):
            print("Scored A grade")

        elif(self.marks >= 75):
            print("Scored B grade")
        
        elif(self.marks >= 50):
            print("Scored C grade")

        else:
            print("Scored F grade")

# create object
s1 = Students("Rohit", 90)
s2 = Students("kabir", 95)
s3 = Students("Dev", 80)

# s1.showDetails()
# s1.showGrade()

students = [s1, s2, s3]

topper = students[0]

for student in students:
    if(student.marks > topper.marks):
        topper = student

print("Topper:", topper.name, "with", topper.marks, "marks")

