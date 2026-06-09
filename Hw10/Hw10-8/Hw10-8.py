'''
(Flattening arrays with flatten vs. ravel) Using the array created in
Exercise 7.4, first, flatten the array with the method flatten. Change the second element
of the new array to 10. Compare the new and the original array. Second, flatten the
array using the method ravel and perform the same comparison.
'''
import numpy as np

A = [10, 8, 6, 4, 2, 0]
B = [0, 2, 4, 6, 8, 10]

# 結合 list A 和 list B 成一個 2D NumPy array
results = np.array([A, B])
print(results)

print(end="\n")

# flatten 陣列扁平方法
flatten_results = results.flatten()
flatten_results[1] = 10

print(results)
print(end="\n")
print(flatten_results) # 不會影響原本的陣列，只影響扁平化後的資料

print(end="\n")

# ravel 陣列扁平方法
ravel_results = results.ravel()
ravel_results[1] = 10

print(results)
print(end="\n")
print(ravel_results) # 不只影響扁平化後的資料，還會影響原本的陣列