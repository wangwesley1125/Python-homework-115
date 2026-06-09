'''
(Indexing and Slicing arrays) Create an array containing the values 1–15,
reshape it into a 3-by-5 array, then use indexing and slicing techniques to perform each
of the following operations: [implement operations (a) to (c) twice, once with positive indexing and once 
with negative indexing]:
a) Select row 2.
b) Select column 4.
c) Select columns 1–3.
d) Select the element that is in row 1 and column 4.
e) Select all elements from rows 1 and 2 that are in columns 0, 2, and 4.
'''
import numpy as np

# 1~15 矩陣
a = np.arange(1, 16).reshape(3, 5)
print(a) 

print(end="\n")

# slicing rows
# a) 第 2 列
row_2 = a[2, :]
print(row_2[::1]) # positive indexing
print(row_2[::-1]) # negative indexing

print(end="\n")

# slicing colums
# b) 第 4 行
column_4 = a[:, 4]
print(column_4[::1]) # positive indexing
print(column_4[::-1]) # negative indexing

print(end="\n")

# c) 第 1 行到第 3 行
colum_1_to_3 = a[:, 1:3]
print(colum_1_to_3[::1]) # positive indexing
print(colum_1_to_3[::-1]) # negative indexing

print(end="\n")

# d) 取第 1 列、第 4 行的值
print(a[1, 4])

print(end="\n")

# e) 取第 1 列和第 2 列且在第 0 行、第 2 行以及第 4 行
print(a[1, 0], a[1, 2], a[1, 4])
print(a[2, 0], a[2, 2], a[2, 4])