import numpy as np

a = np.arange(1, 16).reshape(3, 5)

print(a)

print(end="\n")

print(a[1])

print(end="\n")

print(a[[0, 2]])

print(end="\n")

print(a[:, 1:4])