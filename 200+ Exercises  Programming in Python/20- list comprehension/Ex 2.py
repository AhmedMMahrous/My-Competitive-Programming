from unittest import result


tax = 0.23
net_price = [5.5, 4.0, 9.0, 10.0]

result = [round(i * (1 + tax),2) for i in net_price]
print(f"{result}")