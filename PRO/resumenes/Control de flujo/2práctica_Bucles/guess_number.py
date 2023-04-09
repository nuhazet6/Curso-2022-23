random_number = 87
tries = 0
while True:
    choose = int(input("Introduce un número:"))
    tries += 1
    if choose < random_number:
        print("Mayor")
    elif choose > random_number:
        print("Menor")
    else:
        print(f"¡Felicidades!, has acertado en {tries} intentos :)")
        break
