n = 1   # number of periods (in years)
pv = 1000   # present value
r = 0.04   # interest rate (annual)
fv = pv * (1 + r)   # future value


while fv <= 2000:
    fv = fv * (1 + r)
    n += 1
print(f'Future value: {fv:.2f} USD. Number of periods: {n} years')
