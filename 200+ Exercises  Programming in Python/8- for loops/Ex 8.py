items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
result = []
for i in items:
    if i not in result:
       x = items.count(i)
       result.append(x)
    else:
       print(result)
x = []
for item in result:
    if item not in x:
        x.append(item)
        
print(f"'x':{x[0]}, 'y': {x[1]},'z': {x[2]}")
print(f"Another SOL \n ####################")
freq = {}
for item in items:
    if item not in freq.keys():
        freq[item] = 1
    else:
        freq[item] += 1
 
print(freq)


