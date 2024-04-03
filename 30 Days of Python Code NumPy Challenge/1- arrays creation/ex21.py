import numpy as np
arr = np.arange(0,1.1,0.1).reshape(1,11)
arr1 = np.zeros((4,11))
full_arr = np.concatenate((arr, arr1),axis=0)
print(full_arr)