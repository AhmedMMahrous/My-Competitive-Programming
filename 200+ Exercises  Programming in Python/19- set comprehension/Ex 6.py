omega = [(i,n,g) for i in range(1,7) for n in range(1,7) for g in range(1,7)]
print(len(omega))
result = [num for num in omega if num[0] % 2 != 0 and num[1] % 2 != 0 and num[2] % 2 != 0]
print(f"Probability: {round(len(result)/len(omega),4)}")