gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}
for key, value in gaming.items():
    if value[1] == 'PLN':
        continue
    value[0] = value[0] * 4.0
    value[1] = 'PLN'
print(gaming)
        
