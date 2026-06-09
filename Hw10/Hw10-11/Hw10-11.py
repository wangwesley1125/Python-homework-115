'''
(Pandas: DataFrames) Perform the following tasks with pandas DataFrames:
a) Create a DataFrame named temperatures from a dictionary of three temperature readings each for 'Maxine', 'James' and 'Amanda'.
b) Recreate the DataFrame temperatures in Part (a) with custom indices using
the index keyword argument and a list containing 'Morning', 'Afternoon'
and 'Evening'.
c) Select from temperatures the column of temperature readings for 'Maxine'.
d) Select from temperatures the row of 'Morning' temperature readings.
e) Select from temperatures the rows for 'Morning' and 'Evening' temperature
readings.
f) Select from temperatures the columns of temperature readings for 'Amanda'
and 'Maxine'.
g) Select from temperatures the elements for 'Amanda' and 'Maxine' in the
'Morning' and 'Afternoon'.
h) Use the describe method to produce temperatures’ descriptive statistics.
i) Transpose temperatures.
j) Sort temperatures so that its column names are in alphabetical order.
'''
import numpy as np
import pandas as pd

# a, b)
temperatures = pd.DataFrame(
    {
        'Maxine': [98.6, 98.9, 100.2],
        'James':  [97.5, 98.1, 99.0],
        'Amanda': [99.1, 97.9, 98.4]
    },
    index=['Morning', 'Afternoon', 'Evening']
)

# c)
print(temperatures['Maxine'])

print(end="\n")

# d)
print(temperatures.loc['Morning'])

print(end="\n")

# e)
print(temperatures.loc[['Morning', 'Evening']])

print(end="\n")

# f)
print(temperatures[['Amanda', 'Maxine']])

print(end="\n")

# g)
print(temperatures.loc[
    ['Morning', 'Afternoon'],
    ['Amanda', 'Maxine']
])

print(end="\n")

# h)
print(temperatures.describe())

print(end="\n")

# i)
print(temperatures.T)

print(end="\n")

# j)
print(temperatures.sort_index(axis=1))