empty_list = []
data = ["uno", 2, 5.0]
list("String")  # Conversión
list(range(10))
list()  # lista vacía
data[0]  # obtener un elemento
data[1:]  # trocear una lista
data[::-1]  # invertir una lista conservando la original con troceado
list(reversed(data))  # invertir una lista conservando la original con reversed
data.reverse()  # invertir una lista (modificando la original)
data.append("Atún")  # añadir un elemento al final de la lista
data.insert(1, 7)  # añadir un elemento en cualquier lugar de la lista
data * 3  # repetir los elementos de una lista
data + empty_list  # combinando listas conservando la original
data.extend(empty_list)  # combinando listas modificando la original
data[0] = "random"  # modificar un elemento utilizando su índice
data[1:3] = [3, "madera"]  # modificar varios elementos a la vez con el troceado.
del data[2]  # eliminar un elemento por su índice
data.remove("Atún")  # eliminar un elemento por su valor
tres = data.pop(1)  # eliminar un elemento por su índice extrayéndolo
data[1:3] = []  # eliminar elementos por su rango
data.clear()  # eliminar todos los elementos
data = []  # eliminar todos los elementos pero con una nueva zona de memoria
data = list(range(9))
data.index(
    5
)  # encontrar el índice que corresponde a un valor (si el elemento no está en la lista dará un error)
4 in data  # pertenencia de un elemento
data.count(
    "1"
)  # Devuelve cuántas veces aparece un determinado valor dentro de una lista
", ".join(
    data
)  # convierte una lista en una cadena de texto(string) usando el separador indicado. (solo funciona si todos sus elementos son cadenas de texto)
sorted(data)  # devuelve una nueva lista ordenada
data.sort()  # modifica una lista ordenándola
sorted(data, reverse=True)  # lista ordenada a la inversa
len(data)  # longitud de una lista
for number in data:  # Iterar sobre una lista
    print(number)
for i, number in enumerate(data):  # iterar añadiendo una enumeración a cada fila
    print(i, number)
data2 = list(range(9))
for number1, number2 in zip(data, data2):  # iterar sobre múltiples listas
    print(number1, number2)
# si copiamos una lista, estaremos copiando el lugar de memoria de dicha lista por lo tanto al cambiar la original se cambiaría la copia
# es decir si hacemos copy_data = data y luego data[0] = 15 entonces copy_data[0] = 15
copy_data = (
    data.copy()
)  # copiar solo los datos no la posición de memoria. Así si cambiamos en un lado, no repercute en el otro.
word = "wololo"
is_enough_length = len(word) > 4
is_right_beginning = word.startwith("p")
min_ys = word.count("y") >= 1
is_fine_word = all(
    [is_enough_length, is_right_beginning, min_ys]
)  # se comprueba que se cumplan todas las expresiones.
is_fine_word2 = any(
    [is_enough_length, is_right_beginning, min_ys]
)  # se comprueba que se cumpla alguna de las expresiones.
values = "32,45,11,87,20,48"
int_values = [int(value) for value in values.split(",")]  # lista por compresión
int_values = [
    int(v) for v in values.split(",") if v.startswith("4")
]  # lista por compresión con condiciones.
svalues = values.split(",")
combinations = [
    f"{v1}x{v2}" for v1 in svalues for v2 in svalues
]  # anidamiento en compresiones

import sys

number = int(sys.argv[1])  # numero introducido por linea de comandos
sum(data)  # suma todos los elementos de la lista
min(data)  # halla el mínimo de los elementos de una lista
max(data)  # halla el máximo de los elementos de una lista
