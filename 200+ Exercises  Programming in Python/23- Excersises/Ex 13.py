import numpy as np
def transpose(List):
    arr = np.matrix(List)
    result = arr.transpose()
    return result


print(transpose([[1, 2, 3], [4, 5, 6]]))