items = ('',0.0, 0, False)

for i in items:
    if i == True:        
         print(True)
         break
    else:        
        print(False)
        
print(f"{30*'#'}")
#### Another Sol
print(any(items))
