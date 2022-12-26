def detect_class(List):
    result = []
    for item in List:
        max_value = max(item)
        empty = [0] * len(item)
        for idx , val in enumerate(item):
            if val == max_value:
                empty[idx] = 1
                result.append(empty)

        
    return result

print(detect_class([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2], [0.0, 0.3, 0.3, 0.4]]))
