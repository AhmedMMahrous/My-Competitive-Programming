import numpy as np
l1 = [[1], [2]]
l2 = [[3], [4]]

def concat(x,y):
   result = []
   for i , j in zip(x,y):
    result.append([i[0],j[0]])
   return result
    
print(concat(l1,l2))
