

def my_func(nums):
    x = list(nums)
    if len (x) == len(set(x)):
        return False
    else:
        return True






print(my_func([1,1,1,3,3,4,3,2,4,2]))

