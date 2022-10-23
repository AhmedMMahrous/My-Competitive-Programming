def map_longest(words):

    max_lenth = max([len(word) for word in words])
    print(max_lenth)
        

map_longest(['ahmed','jd','ali','mohamed'])

## Another Sol 

def map_longest(words):
    length = []
    for word in words:
        length.append(len(word))
    return max(length)
print(map_longest(['java', 'sql', 'r']))
