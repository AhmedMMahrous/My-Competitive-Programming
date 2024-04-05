import numpy as np


A1 = np.array([3, 5, 1])
A2 = np.array([3, 5, 1], dtype=np.int8)
A3 = np.array([3, 5, 1], dtype=np.int16)
A4 = np.array([3, 5, 1], dtype='float')

print(A1.nbytes)
print(A2.nbytes)
print(A3.nbytes)
print(A4.nbytes)