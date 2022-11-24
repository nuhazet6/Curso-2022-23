BOARD_SIZE = 8
board_player1 = []
for i in range(BOARD_SIZE):
    board_player1.append([])
    for _ in range(BOARD_SIZE):
        board_player1[i].append("-")
board_player1[4][4] = "G"
SHIPS = [
    ["CARRIER", 5, "@"],
    ["BATTLESHIP", 4, "#"],
    ["CRUISER", 3, "+"],
    ["SUBMARINE", 3, "¬"],
    ["DESTROYER", 2, "~"],
]
ship_size = [0][1]
ship_symbol = [0][2]
while True:
    ship_position = input("Seleccione la posición de la nave del estilo 1,8").split(",")
    x_coord = ship_position[0]
    y_coord = ship_position[1]
    if board_player1[x_coord][y_coord] != "-":
        print("Error. Esa posición está ocupada por un barco")
        continue
    horizontal = 0
    vertical = 0
    ship_orientation = input(
        "Seleccione una orientación:\nizquierda = -1,0 \nderecha = 1,0 \nabajo = 0,-1 arriba = 0,1"
    ).split(",")

    for _ in range(ship_size):
        x_coord += ship_orientation[0]
        y_coord += ship_orientation[1]
        next_x = x_coord + ship_orientation[0]
        next_y = y_coord + ship_orientation[1]
        if board_player1[x_coord][y_coord] != "-" and next_x >= 0 and next_y >= 0:
            print("Error. Fuera de límite del tablero o choque con otro barco.")
    else:
        print("Barco colocado correctamente")
        break
for _ in range(ship_size):
    board_player1[x_coord][y_coord] = ship_symbol
    x_coord -= ship_orientation[0]
    y_coord -= ship_orientation[1]
for i in range

