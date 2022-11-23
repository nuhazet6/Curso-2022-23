BOARD_SIZE = 8
board_player1 = []
for i in range(BOARD_SIZE):
    board_player1.append([])
    for _ in range(BOARD_SIZE):
        board_player1[i].append("-")
board_player2 = board_player1.copy()
CARRIER = [5, "@"]
BATTLESHIP = [4, "#"]
CRUISER = [3, "+"]
SUBMARINE = [3, "¬"]
DESTROYER = [2, "~"]
NUMBER_OF_SHIPS = 5
for i in range(NUMBER_OF_SHIPS):
    input(f"Introduce las coordenadas de la forma fila,columna")
