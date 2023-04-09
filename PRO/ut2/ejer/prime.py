number = 98
for i in range(2, int(number ** (1 / 2)) + 2):
    if number % i == 0:
        print("El número no es primo")
        break
else:
    print("EL número es primo")
