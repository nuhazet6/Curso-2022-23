number1 = int(input("Introduce el primer número:"))
number2 = int(input("Introduce el segundo número:"))
number3 = int(input("Introduce un tercer número:"))


if number1 < number2:
    if number1 < number3:
        min = number1
    else:
        min = number3
elif number1 < number3:
    min = number2
else:
    if number2 < number3:
        min = number2
    else:
        min = number3

if number1 <= number2 and number1 <= number3:
    min = number1
elif number2 <= number1 and number2 <= number3:
    min = number2
elif number3 <= number1 and number3 <= number2:
    min = number3

print(min)
