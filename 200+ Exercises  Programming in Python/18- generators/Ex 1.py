fnames = ['data1.txt', 'data2.txt', 'data3.txt', 'view.jpg']

def file_gen(names):
    result = []
    for name in names:
        if name[-4:]=='.txt':
            result.append(name)
    print(result)

file_gen(fnames)
## Another Sol
def file_gen(fnames):
    for fname in fnames:
        if fname.endswith('.txt'):
            yield fname
