z = {'path1' : 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer',
'path2' : 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-deep-learning-engineer',
'path3' : 'https://e-smartdata.teachable.com/p/sciezka-bi-analyst-data-analyst'}

for key,value in z.items():
    print(f"{key}: {value.find('scientist')}")
