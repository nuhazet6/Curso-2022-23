while True:
    name = input("Introduce tu nombre y apellido en formato título:")
    if name.istitle():
        break
    else:
        print("Error. Debe escribirlo correctamente")


# while not(name := input('Nombre:')).istittle():
#   print('Error')
#
