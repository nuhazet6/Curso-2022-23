BOARD_SIZE = 8
board_player1 = []
for i in range(BOARD_SIZE):
    board_player1.append([])
    for _ in range(BOARD_SIZE):
        board_player1[i].append("-")
board_player2 = board_player1.copy()
SHIPS = [
    ["CARRIER", 5, "@"],
    ["BATTLESHIP", 4, "#"],
    ["CRUISER", 3, "+"],
    ["SUBMARINE", 3, "&"],
    ["DESTROYER", 2, "$"],
]
ORIENTATION = ["A", -1, 0, "B", 1, 0, "C", 0, -1, "D", 0, 1]
player1_ships = ""
for i in range(len(SHIPS)):
    is_ship = False
    while not is_ship:
        ship = input(
            f"Introduce el tipo de barco indicando la letra a la derecha del igual: \nCARRIER (@@@@@) = A \nBATTLESHIP (####), CRUISER, SUBMARINE ó DESTROYER \n"
        )
        for ship_data in SHIPS:
            if ship_data[0] == ship.upper():
                if ship_data[2] not in player1_ships:
                    is_ship = True
                    ship_size = ship_data[1]
                    ship_symbol = ship_data[2]
                    player1_ships += ship_symbol * ship_size
                    break
        else:
            print(
                "No se ha introducido el barco correctamente, error de escritura o el barco ya ha sido colocado"
            )

    # COLOCAR BARCO
    while True:
        ship_position = input(
            "Seleccione la posición de la nave del estilo 1,8 : "
        ).split(",")
        x_coord = int(ship_position[0]) - 1
        y_coord = BOARD_SIZE - int(ship_position[1])
        if board_player1[y_coord][x_coord] != "-":
            print("Error. Esa posición está ocupada por un barco")
            continue
        if not (0 < x_coord < 8) and not (0 < y_coord < 8):
            print("Error. Esa posición está fuera del tablero")
            continue
        ship_orientation = input(
            "Seleccione una orientación, escriba lo indicado a la derecha del igual:\nizquierda = A \nderecha = B \nabajo = C \narriba = D \n"
        ).upper()
        x_index = ORIENTATION.index(ship_orientation) + 1
        ship_x_orientation = ORIENTATION[x_index]
        ship_y_orientation = -(ORIENTATION[x_index + 1])
        for _ in range(ship_size - 1):

            x_coord += ship_x_orientation
            y_coord += ship_y_orientation
            next_x = x_coord + ship_x_orientation
            next_y = y_coord + ship_y_orientation
            if not (-1 <= next_x <= 8) or not (-1 <= next_y <= 8):
                print("Error. Fuera de límite del tablero")
                break
            elif board_player1[y_coord][x_coord] != "-":
                print("Error, el barco ha chocado con otro barco")
                break

        else:
            print("Barco colocado correctamente")
            break

    for _ in range(ship_size):
        board_player1[y_coord][x_coord] = ship_symbol
        x_coord -= ship_x_orientation
        y_coord -= ship_y_orientation
    output = ""
    horizontal_numerations = 8
    print("y")
    for y in board_player1:
        output += str(horizontal_numerations) + " "
        for x in y:
            output += x + " "
        output += "\n"
        horizontal_numerations -= 1
    output += "  1 2 3 4 5 6 7 8 x"
    print(output)

player2_ships = ""
