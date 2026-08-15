print("Hello World!")

name = "Rohit Polkade"
age = 20

'''No special datatype for char, "" or '' both considered as string'''
char = 'R'

print(char)
print(name)
print(age)

'''List!'''
marks = [90, 85, 91, 94]
print(marks)

marks.append(99)
print(marks)

marks.sort()
print(marks)

marks.insert(2, 1)
print(marks)

marks.remove(1)
print(marks)

marks.pop(0)
print(marks)

'''Tuples!'''
tup = (10, 20, 40, 30, 10)
print(tup)

print(tup.count(10))
print(tup.index(30))

'''Slicing'''
print(tup[1: ])
print(tup[:-1])

SingleElementTup = (10,)
print(type(SingleElementTup))

'''Dict!'''
dict = {
   "name" : "Rohit Polkade",
   "age" : 20,
   "skills" : {
        "python" : "Intermediate",
        "java" : "Core",
        "C" : "Beginner"
   }
}
print(dict)

print(dict["name"])
print(dict["skills"]["python"])

print(dict.keys())
print(dict.values())
print(dict.items())
dict.update({"age" : 21 })

print(dict)

'''Sets!'''
set = {1, 2, 3, 4}
print(set)

set.add(5)
print(set)
set.remove(5)
print(set)
set.update([5, 6])
print(set)

set2 ={1, 7, 8}
print(set.union(set2))
print(set | set2)
print(set.intersection(set2))
print(set & set2)
print(set - set2)

'''functions!'''
def sum(num1, num2):
    sum = num1 + num2
    return sum

print(sum(5, 5))


'''Lamda''' 
square = lambda x: x * x
print(square(5))
