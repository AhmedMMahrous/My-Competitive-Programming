desc = "Playway: Playway is a producer of computer games."
desc = desc.lower().replace(':','').replace('.', '').split(' ')
print(len(set(desc)))