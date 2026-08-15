'''Student Performance Matrix Analyzer'''
# Build a NumPy program that combines student marks from multiple classes, performs matrix operations, and generates a final performance report.
import numpy as np

marksA = np.array([[90, 85, 80],
                   [70, 75, 78]])

marksB = np.array([[88, 92, 95],
                   [65, 72, 81]])
print(f"class A:\n{marksA}")
print(f"\nClass B:\n{marksB}")

print("\nMerged Matrix:")
mergedMatrix = np.vstack((marksA, marksB))
print(mergedMatrix)

print(f"\nTranspose:\n {mergedMatrix.T}")

flattenArr = mergedMatrix.flatten()
print(f"\n Flatten:\n {flattenArr}")

add5 = mergedMatrix + 5
print("\n Updated Marks (+5):")
print(add5)
