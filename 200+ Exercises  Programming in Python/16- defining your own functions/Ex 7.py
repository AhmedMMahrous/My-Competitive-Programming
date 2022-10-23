def count_str(List):
    result = [i for i in List if type(i) == str]
    print(len(result))

count_str(['p', 2, 4.3, None])
count_str({'p', 2, 4.3, True, 'True', None})

#### Another Sol
def count_str(items):
    total = 0
    for item in items:
        if isinstance(item, str):
            total += 1
    return total


print(count_str(['p', 2, 4.3, None]))
print(count_str({'p', 2, 4.3, True, 'True', None}))