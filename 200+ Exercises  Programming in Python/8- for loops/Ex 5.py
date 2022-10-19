text = 'Python is a very popular programming language'
items = text.split(' ')
result = [i.lower() for i in items[:4]]
    
print(result)

# another sol
words = text.split(' ')
result = []
for idx, word in enumerate(words):
    if idx < 4:
        result.append(word.lower())
print(result)