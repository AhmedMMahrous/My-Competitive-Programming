def count_str(List):
    result = 0
    for i in List:
        if isinstance(i, str) and len(i) > 2:
            result +=1
    print(result)

count_str([1, '#hello', '', 'python', 'go'])
count_str([1, 2, 3, 'python'])