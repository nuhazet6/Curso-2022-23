# WHILE
want_exit = "N"
num_questions = 0
while want_exit == "N":
    print("Hola qué tal")
    want_exit = input("¿Quiere salir? [S/N] ")
    num_questions += 1
    if want_exit not in "SN":
        want_exit = "N"
        continue  # continue sirve para pasar directamente a la siguiente iteración del bucle, es decir, todo lo que haya debajo del continue dentro del bucle no se ejecutará
    print("Si salgo elegiste N o S :)")
    if num_questions == 4:
        print("Máximo número de preguntas alcanzado")
        break  # break sirve cuando queremos salir de un bucle sin necesidad de que se deje de cumplir la condición del mismo.
else:  # Añadiendo un else a un bucle contemplamos el caso en el que se ha salido del mismo sin usar break
    print("Usted ha decidido salir")
print("Ciao")

# FOR
