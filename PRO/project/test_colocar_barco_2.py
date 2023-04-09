BOARD_SIZE = 8
board_player1 = []
for i in range(BOARD_SIZE):
    board_player1.append([])
    for _ in range(BOARD_SIZE):
        board_player1[i].append("-")
board_player1[4][3] = "G"
SHIPS = [
    ["CARRIER", 5, "@"],
    ["BATTLESHIP", 4, "#"],
    ["CRUISER", 3, "+"],
    ["SUBMARINE", 3, "¬"],
    ["DESTROYER", 2, "o"],
]
ship_size = SHIPS[4][1]
ship_symbol = SHIPS[4][2]
while True:
    ship_position = input("Seleccione la posición de la nave del estilo 1,8 : ").split(
        ","
    )
    x_coord = int(ship_position[0]) - 1
    y_coord = BOARD_SIZE - int(ship_position[1])
    if board_player1[x_coord][y_coord] != "-":
        print("Error. Esa posición está ocupada por un barco")
        continue
    ship_orientation = input(
        "Seleccione una orientación, escriba lo indicado a la derecha del igual:\nizquierda = -1,0 \nderecha = 1,0 \nabajo = 0,-1 \narriba = 0,1 \n"
    ).split(",")
    ship_x_orientation = int(ship_orientation[0])
    ship_y_orientation = -int(ship_orientation[1])
    for _ in range(ship_size - 1):

        x_coord += ship_x_orientation
        y_coord += ship_y_orientation
        next_x = x_coord + ship_x_orientation
        next_y = y_coord + ship_y_orientation
        if not (-1 <= next_x <= 8) or not (-1 <= next_y <= 8):
            print("Error. Fuera de límite del tablero")
            break
        elif board_player1[x_coord][y_coord] != "-":
            print("Error, el barco ha chocado con otro barco")
            break

    else:
        print("Barco colocado correctamente")
        break
for _ in range(ship_size):
    board_player1[x_coord][y_coord] = ship_symbol
    x_coord -= ship_x_orientation
    y_coord -= ship_y_orientation
output = ""
horizontal_numerations = 8
print("y")
for y in range(len(board_player1)):
    output += str(horizontal_numerations) + " "
    for x in range(len(board_player1[y])):
        output += board_player1[x][y] + " "
    output += "\n"
    horizontal_numerations -= 1
output += "  1 2 3 4 5 6 7 8 x"
print(output)
