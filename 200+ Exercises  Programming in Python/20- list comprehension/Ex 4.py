pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]


result_1 = [round(pv * (1 + i)**n , 2) for i in rate]
final_result = [round(n-pv ,2) for n in result_1]
print(final_result)