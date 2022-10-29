omega = [(i,n,g) for i in range(1,7) for n in range(1,7) for g in range(1,7)]
print(len(omega))
result = [num for num in omega if (num[0]+num[1]+num[2]) % 7 == 0]
print(f"Probability: {len(result)/len(omega):.2f}")