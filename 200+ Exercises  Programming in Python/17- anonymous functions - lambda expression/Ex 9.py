num1 = [4, 2, 6, 2, 11]
num2 = [5, 2, 3, 3, 9]

print(list(map(lambda item1,item2: item1 % item2 , num1,num2)))