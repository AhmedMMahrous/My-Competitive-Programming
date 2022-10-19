users = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
user_id = '004'

try:
    print(users[user_id])

except KeyError:
    print('The 004 key is not in the dictionary. Adding key ...')
    users[user_id] = None
print(users)

