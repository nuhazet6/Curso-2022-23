number1 = 12
number2 = 44
if number1 < number2:
    _min = number1
    _max = number2
else:
    _min = number2
    _max = number1
max_div = 1
for i in range(1, _min + 1):
    if _min % i == 0 and _max % i == 0:
        max_div = i
print(max_div)
