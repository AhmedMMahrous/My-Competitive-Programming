def isAnagram(s, t):
        # In case of different length of thpse two strings...
    if len(s) != len(t):
        return False
    else:
        s = sorted(s)
        t = sorted(t)
        if s == t :
            return True
        else:
            return False


print(isAnagram("aacc" , "ccac"))