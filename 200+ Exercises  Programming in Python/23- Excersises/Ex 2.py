y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2, 10.4, 10.8, 11.0]
def MSE(y_true , y_pred):
    result = round(1 / len(y_true) * (sum([abs(i[1] - i[0]) for i in zip(y_true,y_pred)])),4)
    return result

print(MSE(y_true , y_pred))