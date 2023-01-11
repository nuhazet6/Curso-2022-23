# Para escribir en varias líneas lo que el programa va a ejecutar en una se puede usar: 1.barra invertida al final de cada línea menos en la línea final 2.usar paréntesis
# If, elif y else:
temperature = 20
if temperature > 35:
    print("Hace calor")
elif temperature < 10:
    print("Hace frío")
else:
    print("Ta bueno")

# Si solo tenemos un if y un else lo podemos simplificar de la siguiente forma:
fire_risk = "LOW" if temperature < 30 else "HIGH"
print(fire_risk)

# Operadores comparativos: Igualdad == ; Desigualdad != ; Menor que < ; Mayor que > ; Menor o igual que <= ; Mayor o igual que >=
# Operadores lógicos: and or not
if not (temperature < 10):
    print("No está frío")
x = 3
if x > 4 or x == 2:
    print("Se cumplió la primera condicion")
elif x < 4 and x != 2:
    print("Se cumplió la segunda condición")
else:
    print("El número es 4, se llegó al else")

# Valor nulo para comprobar si un valor es nulo se puede usar el operador is, de la forma: if values is None:
# aplicando el operador not tenemos el caso de que el valor no sea nulo
value = 1
if value is not None:
    print(f"{value=}")

# match-case
color = "#FF0000"

match color:

    case "#FF0000":
        print("🔴")
    case "#00FF00":
        print("🟢")
    case "#0000FF":
        print("🔵")
    case _:
        print("Unknown color")

# match_case avanzado
point = (8, 3, 5)

match point:
    case (
        int(x),
        int(y),
    ):  # al introducir en el caso int() obligas a las variables de dentro a ser de tipo int para que se cumpla dicho caso, además se deberán cumplir el número de valores correspondientes(en este caso como la tupla tiene 3 valores int se cumple el segundo caso).
        print(f"({x},{y}) is in plane")
    case (int(x), int(y), int(z)):
        print(f"({x},{y},{z}) is in space")
    case _:
        print("Unknown")

# Operador morsa
radius = 4.25
if (perimeter := 2 * 3.14 * radius) < 100:
    print("Increase radius to reach minimum perimeter")
    print("Actual perimeter: ", perimeter)
