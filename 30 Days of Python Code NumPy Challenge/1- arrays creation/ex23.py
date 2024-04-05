import numpy as np
string_data = '4 2 6 2 7 10 6 2 14'

arr = np.fromstring(string_data, dtype=int, sep=' ')

print(arr)