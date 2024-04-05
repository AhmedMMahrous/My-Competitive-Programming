import numpy as np


arr = np.zeros((3, 8, 4), dtype='int')

arr = arr.reshape(3*8 ,4)
print(arr)