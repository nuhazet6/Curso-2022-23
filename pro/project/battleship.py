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
    ["SUBMARINE", 3, "¬"],
    ["DESTROYER", 2, "~"],
]
player1_ships = ''
for i in range(len(SHIPS)):
    ship = input(
        f"Introduce el tipo de barco: CARRIER, BATTLESHIP, CRUISER, SUBMARINE ó DESTROYER"
    )
    
    while True:
        ship_position = input("Seleccione la posición de la nave del estilo 1,8").split(',')
        if board_player1[ship_position[0]][ship_position[1]] != '-':
            print('Esa posición está ocupada por un barco')
            continue
        horizontal = 0
        vertical = 0
        ship_orientation = input('Seleccione una orientación: izquierda, derecha, abajo, arriba')
        
        horizontal = 
        while True:
            horizontal


player2_ships = ''