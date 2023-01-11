# ***************
# UN SET AL TENIS
# ***************


def run(points: str) -> tuple:
    games_player1 = games_player2 = 0

    PLAYER1 = "A"
    PLAYER2 = "B"
    games_player2 = games_player1 = 0
    player_1_points = player_2_points = 0
    player_1_set = player_2_set = 0
    for point in points:
        if point == PLAYER1:
            player_1_points += 1
        elif point == PLAYER2:
            player_2_points += 1
        else:
            print("Error en el punto")
            break

        result_game = player_1_points - player_2_points
        result_set = games_player1 - games_player2
        # Comprobación de juego de player2
        if player_1_points >= 4 and result_game >= 2:
            games_player1 += 1
            player_1_points = player_2_points = 0
            # Comprobación de set y tiebreak
            tiebreak = games_player1 == 7 and games_player2 == 6
            if games_player1 >= 6 and result_set >= 2 or tiebreak:
                player_1_set += 1
                break
        # Comprobación de juego de player2
        elif player_2_points >= 4 and result_game <= -2:
            games_player2 += 1
            player_1_points = player_2_points = 0
            # Comprobación de set de player2
            tiebreak = games_player1 == 6 and games_player2 == 7
            if games_player2 >= 6 and result_set <= -2 or tiebreak:
                player_2_set += 1
                break

    return games_player1, games_player2


if __name__ == "__main__":
    run("AABBAABABBBABABABBBAAABBBABAABBABBAABBBABABBAAAABBBBABBBAB")
