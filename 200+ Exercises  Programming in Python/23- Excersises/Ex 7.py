import math
def euclidean_distance(x,y):
    result = sum([(i[1] - i[0])**2 for i  in zip(x,y)])
    return math.sqrt(result)

print(euclidean_distance([0, 3], [4, 0]))