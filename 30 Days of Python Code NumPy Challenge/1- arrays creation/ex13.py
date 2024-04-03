import numpy as  np
arr = np.array(
    [
        [4.99, 3.49, 9.99],
        [1.99, 9.99, 14.99],
        [14.99, 2.39, 7.29],
    ]
)

#arr = (arr * 0) + 9.99
# Another Sol
arr = np.full_like(arr, fill_value=9.99)
print(arr)