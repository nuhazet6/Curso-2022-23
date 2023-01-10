# Para escribir en varias líneas lo que el programa va a ejecutar en una se puede usar: 1.barra invertida al final de cada línea menos en la línea final 2.usar paréntesis
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
