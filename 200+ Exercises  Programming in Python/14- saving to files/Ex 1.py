List = []
for i in range(1,20):
    if i % 2 == 0:
        List.append(i)
print(List)

with open('num.txt' ,'w') as file:
    for n in List:
        file.write(str(n) + '\n')
