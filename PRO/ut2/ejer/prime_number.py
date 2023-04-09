number = 11
square_root_number = int(number ** (1 / 2))
for div in range(2, (square_root_number + 1)):
    if number % div == 0:
        print("No es primo")
        break
else:
    print("Es primo")
