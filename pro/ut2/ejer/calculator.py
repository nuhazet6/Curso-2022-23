operator = input("Introduce un operador (+,-,*,/): ")
number1 = int(input("Introduce el primer número: "))
number2 = int(input("Introduce el segundo número: "))

result = None
match operator:
    case "+":
        result = number1 + number2
    case "-":
        result = number1 - number2
    case "/":
        result = number1 / number2
    case "*":
        result = number1 * number2

if result is None:
    print("El operador introducido no es válido")
else:
    print(f"El resultado de {number1} {operator} {number2} es: {result}")
