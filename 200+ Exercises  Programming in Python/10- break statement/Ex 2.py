hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
for i in hashtags:
    if not isinstance(hashtags, str):
         print(False)
         break
    else:
        print(True)
print(f"Another sol \n#######################")

result = True
 
for hashtag in hashtags:
    if not isinstance(hashtag, str):
        result = False
        break
    
print(result)

