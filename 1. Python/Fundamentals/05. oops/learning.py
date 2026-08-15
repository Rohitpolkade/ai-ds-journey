class Student: 
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def printGreet(self):
        print("Hello,", self.name)

s1 = Student("Rohit", 90)
print(s1.name, s1.marks)

s2 = Student("Kabir", 95)
print(s2.name, s2.marks)

s1.printGreet()