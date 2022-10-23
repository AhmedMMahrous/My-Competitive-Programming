def is_palindrome(string):
    inverse = string[::-1]
    if string == inverse:
        return True
    else:
        return False


print(is_palindrome('level'))
print(is_palindrome('python'))