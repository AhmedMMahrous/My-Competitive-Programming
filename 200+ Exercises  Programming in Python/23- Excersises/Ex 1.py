y_true = [0, 0, 1, 1, 0, 1, 0]
y_pred = [0, 0, 1, 0, 0, 1, 0]

def accurcy(y_true , y_pred):
    counter = 0
    for i , j in zip(y_true , y_pred):
        if i == j:
            counter+=1
    return round(counter/len(y_pred),4)

print(accurcy(y_true,y_pred))



