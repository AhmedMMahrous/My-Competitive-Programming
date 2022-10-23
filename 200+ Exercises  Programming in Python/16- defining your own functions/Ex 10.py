def is_distinct(List):
    if list(set(List)) == List:
        return True
    else:
        return False
print(is_distinct([1,2,3]))
print(is_distinct([1,2,3,3]))

## Another Sol
def is_distinct(items):
    return len(items) == len(set(items))

