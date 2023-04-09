number1 = 0
number2 = 1
for _ in range(100):
    print(number1)
    number1_old = number1
    number1 = number2
    number2 += number1_old
