def top_n(List,n):
    List.sort(reverse = True)
    return List[:n]
print(top_n([4, 5, 2, 9, 5, 2, 8, 2, 8, 10], 3))


