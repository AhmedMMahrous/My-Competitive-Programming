stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}

result = {key:value for key ,value in stocks.items() if value > 100}
print(result)