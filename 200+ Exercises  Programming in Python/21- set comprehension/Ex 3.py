omega = [(i,n) for i in range(1,7) for n in range(1,7)]
result = [ num for num in omega if num[0]**2 + num[1]**2 >= 45 ]
print(f"Probability: {len(result)/len(omega):.2f}")