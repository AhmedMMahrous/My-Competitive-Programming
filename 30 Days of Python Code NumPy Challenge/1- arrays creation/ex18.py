import numpy as np


title = '30 Days of Python Code - Numpy Challange'

arr =title.split(' ')
#Reshaping the array into a matrix with 2 rows and -1 columns 
print(np.array(arr).reshape(2,-1))  