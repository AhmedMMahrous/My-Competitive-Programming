import numpy as np


A = np.array([[3, 2, 1, np.nan],
              [5, np.nan, 1, 6]])

for arr in A:
    print(np.isnan(arr))