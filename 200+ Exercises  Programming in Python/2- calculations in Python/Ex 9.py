import math 
  
  
# function for finding roots
def equationroots( a, b, c):
    delta = b ** 2 - 4 * a * c
    delta_sqrt = math.sqrt(delta)
    x1 = (-b - delta_sqrt) / (2 * a)
    x2 = (-b + delta_sqrt) / (2 * a)
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
  


equationroots(1,5,4)