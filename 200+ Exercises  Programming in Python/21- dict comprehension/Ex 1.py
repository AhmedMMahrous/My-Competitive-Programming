
    
keys = [ key for key in range(1,8)]
print(keys)
values = [ value**2 for value in keys]
print(values)
Dict = dict(zip(keys, values))

print(Dict)
# Another Sol
result = {i:i**2 for i in range(1, 8)}
print(result)

