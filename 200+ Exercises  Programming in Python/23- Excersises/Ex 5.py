import numpy as np
items = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = []
for i in items:
    result.extend(i)
print(result)

#Another Sol
def flatten(x):
    x = np.array(x)
    return x.reshape(1,-1)

print(flatten(items))