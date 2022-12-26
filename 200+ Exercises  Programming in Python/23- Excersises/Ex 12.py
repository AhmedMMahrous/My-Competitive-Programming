import numpy as np
def trace(List):
    arr = np.matrix(List)
    result = arr.trace()
    return result

print(trace([[3, 4, 5], [5, 2, 1], [5, 7, 2]]))