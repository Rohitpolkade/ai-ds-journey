# concepts: functions, parameters, args, kwargs

def greet(name):
    print("Hello", name)

greet("Rohit")

'''parameterized function!'''
def add(a, b):
    return a + b

result = add(4, 6)
print(result)


'''*args'''
def totalNumbers(*numbers):
    print("Numbers:", numbers)

totalNumbers(1, 2, 3, 4)


'''**kwargs'''
def studentDetails(**details):
     print("Student Details:", details)

studentDetails(name= "Rohit", age= 20, sem = 5)
