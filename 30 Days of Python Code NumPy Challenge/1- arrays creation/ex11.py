import numpy as np
arr = np.zeros(shape=(6,6) ,dtype='int')
print(arr)
arr[ : : 2 , : : 2] = 2
arr[ 1: : 2 , : : 2] = 4

print(arr)
