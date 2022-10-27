def enum(items):
    idx = 0
    for item in items:
        yield (idx, item)
        idx += 1

print(list(enum(['TEN', 'CDR', 'BBT'])))