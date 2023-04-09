person1 = "piedra"
person2 = "papel"
if person1 == person2:
    winner = 0
elif person1 == "piedra":
    if person2 == "tijera":
        winner = 1
    elif person2 == "papel":
        winner = 2
    else:
        print(
            "Error, no se ha escrito correctamente la entrada (piedra, papel o tijera)"
        )
elif person1 == "papel":
    if person2 == "piedra":
        winner = 1
    elif person2 == "tijera":
        winner = 2
    else:
        print(
            "Error, no se ha escrito correctamente la entrada (piedra, papel o tijera)"
        )
elif person1 == "tijera":
    if person2 == "papel":
        winner = 1
    elif person2 == " piedra":
        winner = 2
    else:
        print(
            "Error, no se ha escrito correctamente la entrada (piedra, papel o tijera)"
        )
else:
    print("Error, no se ha escrito correctamente la entrada (piedra, papel o tijera)")

if winner == 0:
    print("Empate")
else:
    print(f"Gana el jugador {winner}")
