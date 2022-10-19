from enum import unique
from unittest import result


items = [1, 5, 3, 2, 2, 4, 2, 4]
result = []

for item in items:
    if item not in result:
        result.append(item)
        
print(result)




