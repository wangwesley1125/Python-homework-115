'''
(array from List of Lists) Create an array from a list of two lists. The first list consists of the even numbers 
counting down from 10 to 0 and the second counting up from 0 to 10.
'''
import numpy as np

A = [10, 8, 6, 4, 2, 0]
B = [0, 2, 4, 6, 8, 10]

# 結合 list A 和 list B 成一個 2D NumPy array
results = np.array([A, B])
print(results)