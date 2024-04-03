import numpy as np
arr = np.array([[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]])

#arr = np.ones(shape=(4, 4), dtype='int')
arr = np.pad(arr * 5, pad_width=1, constant_values=0)
print(arr)
