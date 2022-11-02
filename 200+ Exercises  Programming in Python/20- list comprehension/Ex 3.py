pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]

result = [round(pv * (1 + i)**n , 2) for i in rate]
print(result)