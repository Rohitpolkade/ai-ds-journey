import numpy as np

marks = np.array([10, 20, 30, 40, 50])
print("marks:", marks)
print(type(marks))

"""operation -- vectorization"""
print(marks + 15)
print(marks * 2)
print(marks / 5)

"""functions -- statistics"""
print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))
print(np.sum(marks))
# var - variance
print(np.var(marks))
# std - standard deviation
print(np.std(marks)) 

"""operation -- vectorization"""
print(marks + 15)
print(marks * 2)
print(marks / 5)

"""functions -- statistics"""
print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))
print(np.sum(marks))
# var - variance
print(np.var(marks))
# std - standard deviation
print(np.std(marks)) 


"""Filtering -- Boolean Indexing/ masking"""   
print(marks > 30) 

mask = marks > 30
filteredArr = marks[mask]
print(filteredArr)
# or
print(marks[marks > 30])

"""Zeros & Ones"""
zerosArr = np.zeros(10)
print(zerosArr)

onesArr = np.ones(10)
print(onesArr)

numbArr = np.full(10, 5)
print(numbArr)

"""Arange"""
arr = np.arange(0, 11, 2)
print(arr)

"""Identity Matrix"""
identityMatrix = np.eye(3)
print(identityMatrix)

"""Random Numbers"""
randomArr = np.random.randint(1, 50, 10)
print(randomArr)

