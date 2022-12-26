def fill_values(height,width,value):
    result = [[value] * width for i in range(height)]
    return result

print(fill_values(3,1,3))