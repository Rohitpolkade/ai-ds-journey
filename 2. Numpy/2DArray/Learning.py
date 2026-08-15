
import numpy as np
marks = np.array([
         [90, 91, 80],
         [86, 80, 88],
         [78, 90, 86]
         ])

print(marks)
print(marks.shape)
print(marks.size)
print(marks.ndim)
print(marks.dtype)

"""Indexing"""
print(marks[0])
print(marks[0, 1])

arr = np.array([1,2,3,4,5,6])
print(arr[[0,2,4]])

"""Slicing"""
print(arr[0])
print(marks[:,1])
print(arr[1:5])

"""Reshaping"""
print(arr.reshape(2,3))

"""Matrix Operations"""
A = np.array([[2, 3],
              [4, 5]])

B = np.array([[6, 4],
             [3, 2]])

print(A + B)
print(B - A)

# Matrix multiplicaion
print(A @ B)
# or
print(np.dot(A, B))

# Elementwise multiplication
print(A * B)

'''Flatten'''
arr2D = np.array([[1, 2, 3],
                  [4, 5, 6]])

print(arr2D.flatten())
print(arr2D)
print()
print(arr2D.ravel())
print(arr2D)


'''Manipulation'''
# Insertion
rowAdd = np.insert(arr2D, 3, (8, 9), 1)
print(rowAdd)

# append
print(np.append(arr2D, [[1,2,4]], axis = 0))

# concatenation
A = np.array([1,2])
B = np.array([3, 4])
print(np.concatenate((A, B)))

# deletion
print(np.delete(A, 0))
print(np.delete(arr2D, 0, axis = 0))

'''Stacking'''
print(np.vstack((A, B)))
print(np.hstack((A, B)))

'''BoardCasting'''
print(A + B)
print(A + 10)
