# *****************
# UN JUEGO AL TENIS
# *****************


def run(points: str) -> str:
    player_A_points = player_B_points = 0
    PLAYER1 = "A"
    PLAYER2 = "B"
    for point in points:
        if point == PLAYER1:
            player_A_points += 1
        elif point == PLAYER2:
            player_B_points += 1
        else:
            print("Error en el punto, n")
            break
        result_game = player_A_points - player_B_points
        if player_A_points >= 4 and result_game >= 2:
            winner = PLAYER1
        else:
            winner = PLAYER2
    return winner


if __name__ == "__main__":
    run("ABAABA")
