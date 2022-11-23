from genericpath import exists


number1 = float(input("Introduce un número: "))
number2 = float(input("Introduce otro número: "))
operator = input("Introduce un operador: ")

match operator:
    case "+":
        result = number1 + number2
    case "-":
        result = number1 - number2
    case "/":
        result = number1 / number2
    case "*":
        result = number1 * number2
    case _:
        result = None

if result is not None:
    print(f"{number1} {operator} {number2} = {result}")
else:
    print("Error, no se ha introducido un operando válido")
