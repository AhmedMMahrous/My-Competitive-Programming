def sort_list(items):
    return sorted(items, key=lambda item: item[1])

print(sort_list(([(1, 3), (4, 1), (4, 2), (0, 7)])))
