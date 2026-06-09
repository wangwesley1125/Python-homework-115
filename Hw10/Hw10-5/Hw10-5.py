'''
(Broadcasting) Use arange to create a 2-by-2 array containing the numbers 0–3.
Use broadcasting to perform each of the following operations on the original array:
a) Cube every element of the array.
b) Add 7 to every element of the array.
c) Multiply every element of the array by 2.
'''
import numpy as np

A = np.array([
    [0, 1],
    [2, 3]
])

print(A**3)

print(end="\n")

print(A+7)

print(end="\n")

print(A*2)