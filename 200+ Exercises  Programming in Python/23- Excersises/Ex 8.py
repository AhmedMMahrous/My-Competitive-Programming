def arrange(start,end,step = 1):
    result = []
    for i in range(start,end,step):
        result.append(i)
    return result

print(arrange(1,10))
print(arrange(1,10,2))