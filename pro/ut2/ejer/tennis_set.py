# ***************
# UN SET AL TENIS
# ***************


def run(points: str) -> tuple:
    games_player1 = games_player2 = 0

    PLAYER1 = "A"
    PLAYER2 = "B"
    IS_TIEBREAK = 6
    DISTANCE_TO_WIN = 2
    games_player2 = games_player1 = 0
    player_1_points = player_2_points = 0
    min_point_to_win = 4
    for point in points:
        if point == PLAYER1:
            player_1_points += 1
        elif point == PLAYER2:
            player_2_points += 1
        else:
            print("Error en el punto")
            break

        result_game = player_1_points - player_2_points
        # Comprobación de juego de player1
        if player_1_points >= min_point_to_win and result_game >= DISTANCE_TO_WIN:
            games_player1 += 1
            player_1_points = player_2_points = 0
        # Comprobación de juego de player2
        elif player_2_points >= min_point_to_win and result_game <= -DISTANCE_TO_WIN:
            games_player2 += 1
            player_1_points = player_2_points = 0

        # Comprobación de juego tiebreak
        if player_1_points == player_2_points == 0:
            if games_player1 == games_player2 == IS_TIEBREAK:
                min_point_to_win = 7
            else:
                min_point_to_win = 4

    return games_player1, games_player2


if __name__ == "__main__":
    run("AABBAABABBBABABABBBAAABBBABAABBABBAABBBABABBAAAABBBBABBBAB")
