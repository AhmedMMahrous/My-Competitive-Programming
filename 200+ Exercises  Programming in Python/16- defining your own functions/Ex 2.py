def maximum(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= z:
        return y
    else:
        return z

print(maximum(4, 2, 1))
