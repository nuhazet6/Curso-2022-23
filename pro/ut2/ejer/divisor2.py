a = 100
b = 50

_min = a if a < b else b

for divisor in range(_min, 0, -1):
    if a % divisor == 0 and b % divisor == 0:
        mcd = divisor
        break
else:
    mcd = 1

print(mcd)
