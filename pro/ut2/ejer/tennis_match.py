match = "BABABAABBBBABABAABBBBABABAABBBBABABAABBBBABABAABBBBABABAABBBAABABABABAABBBBAABAAABAAABBAABBABABAAAAABABABABAABBBBBBAAAABABBAAABABABAABBBBABABAABBBBABABAABBBBABABAABBBBABABAABBBBABABAABBB"
PLAYER1 = "A"  # AABABABABAABBBBAABAAABAAABBAABBABABAAAAABABABABAABBBBBBAAAABABBAAA
PLAYER2 = "B"  # BABABAABBBBABABAABBBBABABAABBBBABABAABBBBABABAABBBBABABAABBB
player_B_set = player_A_set = 0
player_B_games = player_A_games = 0
player_A_points = player_B_points = 0
for point in match:
    if point == PLAYER1:
        player_A_points += 1
    elif point == PLAYER2:
        player_B_points += 1
    else:
        print("Error en el punto")
        break

    result_game = player_A_points - player_B_points
    result_set = player_A_games - player_B_games
    if player_A_points >= 4 and result_game >= 2:
        player_A_games += 1
        player_A_points = player_B_points = 0

        tiebreak = player_A_games == 7 and player_B_games == 6
        if player_A_games >= 6 and result_set >= 2 or tiebreak:
            player_A_set += 1
            player_A_games = player_B_games = 0
            if player_A_set >= 2:
                winner = PLAYER1
    elif player_B_points >= 4 and result_game <= -2:
        player_B_games += 1
        player_A_points = player_B_points = 0
        
        tiebreak = player_A_games == 6 and player_B_games == 7
        if player_B_games >= 6 and result_set <= -2 or tiebreak:
            player_B_set += 1
            player_A_games = player_B_games = 0
            if player_B_set >= 2:
                winner = PLAYER2


print(
    f"El jugador 1 tiene: {player_A_set} sets\nEl jugador 2 tiene: {player_B_set} sets \nEl ganador es: {winner}"
)
