with open(r'200+ Exercises  Programming in Python\20- list comprehension\plw.txt' ,'r') as file:
    text = file.readlines()




line = [ word for word in text if len(word) > 0]
result = [i.split() for i in line]
print(result)
