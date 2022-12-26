def count_none(List):
    result = 0
    for i in List:
        if i == None:
            result+=1
    return result
print(count_none([1,None,2,None,None]))