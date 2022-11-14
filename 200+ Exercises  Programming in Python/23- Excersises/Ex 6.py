def transfer_zeroes(x):
    for i in x:
        if i == 0:
            x.remove(i)
            x.append(0)
    print(x)
    
            
transfer_zeroes([3, 4, 0, 2, 0, 5, 1, 6, 2])
# Another Sol
def transfer_zeros(items):
    result = []
    counter = 0
    for item in items:
        if item == 0:
            counter += 1
        else:
            result.append(item)
    result.extend([0] * counter)
    return result

print(transfer_zeros([3, 4, 0, 2, 0, 5, 1, 6, 2]))