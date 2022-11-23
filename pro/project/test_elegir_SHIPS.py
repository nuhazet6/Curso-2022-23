SHIPS = [
    ["CARRIER", 5, "@"],
    ["BATTLESHIP", 4, "#"],
    ["CRUISER", 3, "+"],
    ["SUBMARINE", 3, "¬"],
    ["DESTROYER", 2, "~"],
]

player1_ships = "@@@@@"
is_ship = False
while not is_ship:
    ship = input(
        f"Introduce el tipo de barco: CARRIER, BATTLESHIP, CRUISER, SUBMARINE ó DESTROYER \n"
    )
    for ship_data in SHIPS:
        if ship_data[0] == ship.upper():
            if ship_data[2] not in player1_ships:
                is_ship = True
                break
    else:
        print("No se ha introducido el barco correctamente")
