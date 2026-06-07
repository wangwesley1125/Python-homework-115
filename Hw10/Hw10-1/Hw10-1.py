import numpy as np

a = np.arange(1, 7).reshape(2, 3)

a = np.hstack((a, a))

a = np.vstack((a, a))

print(a)