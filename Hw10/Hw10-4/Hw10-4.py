'''
(Filling arrays) Fill a 2-by-3 array with ones, a 3-by-3 array with zeros and a 2-
by-5 array with 7s.
'''
import numpy as np

# 2x3 array
matrix_one = np.array([
    [1, 1, 1],
    [1, 1, 1]
])

print(f"{matrix_one}")

print(end="\n")

# 3x3 array
matrix_zero = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
])

print(f"{matrix_zero}")

print(end="\n")

# 2x5 array
matrix_seven = np.array([
    [7, 7, 7, 7, 7],
    [7, 7, 7, 7, 7]
])

print(f"{matrix_seven}")