'''
(Element-Wise array Multiplication) Create a 10-by-10 array containing the
number 4 in each position. Create a second 10-by-10 array containing the numbers 1 to
100 in ascending order. Multiply the first array by the second array.
'''
import numpy as np

# 每個元素為 4 的 10x10 array
A = np.full((10, 10), 4)

print(A)

print(end="\n")

# 1~100 的 10x10 array
B = np.arange(1, 101).reshape(10, 10)

print(B)

print(end="\n")

# A x B
print(A*B)