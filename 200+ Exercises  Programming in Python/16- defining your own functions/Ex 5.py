def filter_ge_6(words):

    List = [word for word in words if len(word) >= 6]
    print(List)

filter_ge_6(['programming', 'python', 'java', 'sql'])
filter_ge_6(['java', 'sql'])