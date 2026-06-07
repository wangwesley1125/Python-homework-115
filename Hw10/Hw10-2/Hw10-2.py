import numpy as np
import pandas as pd

temps = np.random.randint(60, 101, 6)

temperatures = pd.Series(temps)

print(f"{temperatures}\n")

print(f"{temperatures.min()}\n")

print(f"{temperatures.max()}\n")

print(f"{temperatures.mean()}\n")

print(f"{temperatures.describe()}")