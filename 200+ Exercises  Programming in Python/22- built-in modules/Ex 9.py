from collections import Counter
items = ['YES', 'NO', 'NO', 'YES', 'EMPTY', 'YES', 'NO']
count = Counter()
for i in items:
    count[i]+=1
print(count)

# Another Sol
result = dict(zip(list(items),[list(items).count(i) for i in list(items)]))
print(f'Counter({result})')
