with open(r'200+ Exercises  Programming in Python\13- reading files\Ex 2 currencies.txt' ,'r') as file:
    lines = file.read().splitlines()

for i in lines:
    if 'USD' in i:
        print(i)