with open(r'200+ Exercises  Programming in Python\13- reading files\Ex 3 playway.csv' ,'r') as file:
    content = file.read().splitlines()



data = [(line.split(',')[0], line.split(',')[-1]) for line in content]
data = [(val[0], int(val[1])) for val in data[1:]]
max_vol = max([val[1] for val in data])
max_date = list(filter(lambda val: val[1] == max_vol, data))[0][0]
print(f'Date: {max_date}')