def sum_up(*args):
    s = 0
    for i in args:
        s += i
    return s
print(f"The sum of the sequence: {sum_up(1,0.5,0.25,0.125)}")