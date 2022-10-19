from cmath import sqrt


import math
def stdv(*args):
    n = len(args)
    mean = sum(args) / n
    std = [(k - mean)**2 for k in args]
    final_std = sum(std) / n
    print(f"The standard deviation: {math.sqrt(final_std):0.2f}")
stdv(10,11,9)

