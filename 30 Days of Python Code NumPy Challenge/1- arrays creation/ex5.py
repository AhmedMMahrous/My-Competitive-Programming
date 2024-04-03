import numpy as np
arr = np.zeros(((7,8)) , dtype='int16')
np.fill_diagonal(arr,1) #OR
#arr = np.eye(N=8, dtype='int16')

print(arr)