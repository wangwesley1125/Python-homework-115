import pandas as pd

temps = {'Mon':[68, 89], 'Tue':[71, 93], 'Wed':[66, 82], 'Thu':[75, 97], 'Fri':[62, 79]}

# (a)
temperatures = pd.DataFrame(temps, index=['Low', 'High'])
print(f"{temperatures}\n")

 # (b)
print(f"{temperatures.loc[:, 'Mon':'Wed']}\n")

# (c)
print(f"{temperatures.loc['Low']}\n")

# (d)
pd.set_option('display.precision', 2) # 新版的 panda 改語法了
print(f"{temperatures.mean()}\n")

# (e)
print(temperatures.mean(axis=1))