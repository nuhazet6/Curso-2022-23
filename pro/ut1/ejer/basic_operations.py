number1 = int(input("Introduce un número:"))
number2 = int(input("Introduce otro número:"))

result = number1 + number2
print(number1, "+", number2, "=", result, sep="")

result = number1 - number2
print(number1, "-", number2, "=", result, sep="")

result = number1 * number2
print(number1, "*", number2, "=", result, sep="")

result = number1 / number2
print(number1, "/", number2, "=", result, sep="")


result = number1 + number2
print(number1, number2, sep="+", end="=")
print(result)

result = number1 - number2
print(number1, number2, sep="-", end="=")
print(result)

result = number1 * number2
print(number1, number2, sep="*", end="=")
print(result)

result = number1 / number2
print(number1, number2, sep="/", end="=")
print(result)

print(number1, "/", number2, "=", result, sep="")
