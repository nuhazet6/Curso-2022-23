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

# FOR -> sirve para recorrer un iterable (for-each en java y otros lenguajes)
for _ in range(
    3
):  # range genera un objeto iterable que podemos aprovechar para recorrer un rango personalizado, las opciones son: range(start, stop, step) start: es opcional y tiene valor por defecto 0 stop: es obligatorio (siempre se llega a 1 menos que este valor) step: es opcional y tiene valor por defecto 1; por otra parte si no vamos a usar la variable que toma valores en el rango debemos poner guión bajo _
    print("Repeat me 3 times")
# anidamiento
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print(
            f"{i} * {j} = {result}"
        )  # Estos bucles anidados imprimirán las tablas de multiplicar del 1 al 9, la forma de funcionar es que en la primera vuelta de la i, cuando vale 1, se mete dentro del bucle j y hasta que j no vale 9 no salta a la siguiente iteración del bucle i, en la que vale 2,
