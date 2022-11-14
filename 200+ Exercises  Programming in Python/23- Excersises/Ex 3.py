y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2, 10.4, 10.8, 11.0]

def mse(y_true,y_ypred):
    result = sum([((abs(i[1] - i[0])))**2 / len(y_true) for i in zip(y_true,y_pred)])
    return round(result , 3)

print(mse(y_true,y_pred))