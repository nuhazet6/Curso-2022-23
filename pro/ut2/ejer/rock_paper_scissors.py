person1 = input("Introduce 'piedra' 'papel' o 'tijera' para el jugador1: ")
person2 = input("Introduce 'piedra' 'papel' o 'tijera' para el jugador2: ")
winner = -1
is_rock_person1 = person1 == "piedra"
is_rock_person2 = person2 == "piedra"
is_paper_person1 = person1 == "papel"
is_paper_person2 = person2 == "papel"
is_scissor_person1 = person1 == "tijera"
is_scissor_person2 = person2 == "tijera"

if is_rock_person1 and is_rock_person2:
    winner = 0
elif is_rock_person1 and is_paper_person2:
    winner = 2
elif is_rock_person1 and is_scissor_person2:
    winner = 1

elif is_paper_person1 and is_rock_person2:
    winner = 1
elif is_paper_person1 and is_paper_person2:
    winner = 0
elif is_paper_person1 and is_scissor_person2:
    winner = 2

elif is_scissor_person1 and is_rock_person2:
    winner = 2
elif is_scissor_person1 and is_paper_person2:
    winner = 1
elif is_scissor_person1 and is_scissor_person2:
    winner = 0

winner_phrase = ""
winner_weapon = ""
if winner == 1:
    winner_phrase += "Gana persona1: "
    winner_weapon = person1
elif winner == 2:
    winner_phrase += "Gana persona2: "
    winner_weapon = person2
elif winner == 0:
    winner_phrase += "Empate"

if winner_weapon == "piedra":
    winner_phrase += "piedra rompe tijera"
elif winner_weapon == "papel":
    winner_phrase += "papel envuelve piedra"
elif winner_weapon == "tijera":
    winner_phrase += "tijera corta papel"

if winner_phrase != "":
    print(winner_phrase)
else:
    print("Los datos introducidos no son válidos")


player1 = input("Introduce  ")
