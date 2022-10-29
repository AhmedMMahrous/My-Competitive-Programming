omega = {(i, j) for i in range(1, 7) for j in range(1, 7)}
print(len(omega))
result = {pair for pair in omega if pair[0] + pair[1] > 10}
print(len(result))
print(f'Probability: {len(result) / len(omega):.2f}')

