var1 = 'Python'
var2 = ('Python')
var3 = ('Python',)
var4 = ['Python']
var5 = {'Python'}

List = [var1 , var2 , var3 , var4 , var5]

for i in List:
    print(isinstance(i,tuple))
    