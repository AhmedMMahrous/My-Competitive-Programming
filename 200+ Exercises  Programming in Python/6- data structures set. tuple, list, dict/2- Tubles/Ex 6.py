info = (('Monica', 19), ('Tom', 21), ('John', 18))
asc = tuple(sorted(info, key=lambda item: item[1]))
desc = tuple(sorted(info, key=lambda item: item[1], reverse=True))
print(f'Ascending: {asc}')
print(f'Descending: {desc}')


