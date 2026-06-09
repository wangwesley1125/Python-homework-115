'''
(Pandas: Series) Perform the following tasks with pandas Series:
a) Create a Series from the list [7, 11, 13, 17].
b) Create a Series with five elements that are all 100.0.
c) Create a Series with 20 elements that are all random numbers in the range 0 to
100. Use method describe to produce the Series’ basic descriptive statistics.
d) Create a Series called temperatures of the floating-point values 98.6, 98.9,
100.2 and 97.9. Using the index keyword argument, specify the custom indices 'Julie', 'Charlie', 'Sam' and 'Andrea'.
e) Form a dictionary from the names and values in Part (d), then use it to initialize
a Series.
'''
import numpy as np
import pandas as pd

# a)
a = pd.Series([7, 11, 13, 17])
print(a)

print(end="\n")

# b)
b = pd.Series([100.0, 100.0, 100.0, 100.0, 100.0])
print(b)

print(end="\n")

# c)
rands = np.random.randint(1, 101, 20)
random_nums = pd.Series(rands)
print(random_nums.describe())

print(end="\n")

# d)
temperatures = pd.Series([98.6, 98.9, 100.2, 97.9], index = ['Julie', 'Charlie', 'Sam', 'Andrea'])
print(temperatures)

print(end="\n")

# e)
dic_data = {'Julie':98.6, 'Charlie':98.9, 'Sam':100.2, 'Andrea':97.9}
results = pd.Series(dic_data)
print(results)