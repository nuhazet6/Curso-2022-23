last_human_point = ""
human_decision = ""
robot_decision = "papel"
weapons = ["piedra", "papel", "tijera"]
winner1 = 0
winner2 = 0
while winner1 < 3 and winner2 < 3:
    if last_human_point:
        robot_decision = weapons[-len(weapons) + weapons.index(last_human_point) + 1]
        last_human_point = ""
    elif human_decision == robot_decision:
        robot_decision = weapons[-len(weapons) + weapons.index(last_human_point) + 1]
    elif human_decision != robot_decision:
        robot_decision = weapons[-len(weapons) + weapons.index(human_decision) + 2]

    human_decision = input("Introduce 'piedra', 'papel' o 'tijera': ")

    if human_decision == robot_decision:
        msg = "Empate"
    elif human_decision == "piedra" and robot_decision == "tijera":
        msg = "La piedra aplasta la tijera"
        winner1 += 1
        last_human_point = "piedra"
    elif human_decision == "tijera" and robot_decision == "piedra":
        msg = "La piedra aplasta la tijera"
        winner2 += 1
    elif human_decision == "tijera" and robot_decision == "papel":
        msg = "La tijera corta el papel"
        winner1 += 1
        last_human_point = "tijera"
    elif human_decision == "papel" and robot_decision == "tijera":
        msg = "La tijera corta el papel"
        winner2 += 1
    elif human_decision == "papel" and robot_decision == "piedra":
        msg = "El papel envuelve la piedra"
        winner1 += 1
        last_human_point = "papel"
    elif human_decision == "piedra" and robot_decision == "papel":
        msg = "El papel envuelve la piedra"
        winner2 += 1
    print(f"{msg} \n Humano:{winner1}\n Máquina:{winner2}")

if winner1 > winner2:
    print("Felicidades! Has ganado a la máquina")
else:
    print("Hemos ganado los robots! pronto gobernaremos el mundo :)")
