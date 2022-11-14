import numpy as np
def identity(n):
    result = np.identity(n)
    return result
print(identity(4))

# Another Sol

def identity(n):
    array = [[0]*n for i in range(n)]
    for idx, item in enumerate(array):
        item[idx] = 1
    return array

print(identity(4))