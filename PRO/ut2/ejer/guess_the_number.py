import random

target_number = random.randint(0, 100)
chosed_number = None
tries = 1
while target_number != chosed_number:
    chosed_number = int(input("Elige un número:"))
    if chosed_number < target_number:
        print("Mayor")
    elif chosed_number > target_number:
        print("Menor")
    else:
        print(f"¡Enhorabuena! Has encontrado el número en {tries} intentos")
    tries += 1
