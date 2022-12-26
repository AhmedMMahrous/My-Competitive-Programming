import numpy as np
def dot_product(arr1,arr2):
    result = sum([i * j for i,j in zip(arr1,arr2)])
    return result

print(dot_product([1, 2], [5, 2]))

## Another Sol

def dot(x,y):
    z = np.dot(x,y)
    return z
print(dot([1, 2], [5, 2]))
