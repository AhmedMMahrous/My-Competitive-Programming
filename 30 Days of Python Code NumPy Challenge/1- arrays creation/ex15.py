import numpy as np

A = np.array(
    [
        [False, True, True, False, True],
        [False, False, True, True, True],
    ]
)
# Convert to int type and print the array
print(A.astype('int8'))  