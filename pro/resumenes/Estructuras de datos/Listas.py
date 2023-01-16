# Lista vacía
empty_list = []
# Conversión
list("Python")  # resultado= ['P', 'y', 't', 'h', 'o', 'n']
# Operaciones
# Obtener un elemento
shopping = ["Agua", "Huevos", "Aceite"]
shopping[0]  # Resultado = 'Agua'
# Los índices funcionan como los strings. Los troceados también son iguales
shopping[0:2]  # Resultado= ['Agua','Huevos'], es lo mismo que escribir shopping[:2]
# Invertir una lista: se puede hacer con troceado como se ha visto en los strings [::-1] o con la función reversed() o la función reverse, la diferencia la vemos ahora:
# invertir con troceado: [::-1] -> se conserva la lista original
# invertir con reversed: list(reversed(shopping)) -> se conserva la lista original
# invertir con reverse: shopping.reverse() -> modificando la lista original
# Añadir elementos a la lista
shopping.append(
    "Atún"
)  # Con la función append() se agregan elementos al final de la lista
shopping.insert(
    1, "Jamon"
)  # Con la función insert() se agregan elementos en cualquier lugar de la lista
print(shopping)  # El resultado es: ['Agua', 'Jamon', 'Huevos', 'Aceite', 'Atún']
# Repetir elementos: Con el operador * se pueden repetir los elementos de una lista las veces que indiquemos
# Combinar listas
# Con el operador + o +=: shopping + otra_lista -> conserva la lista original, es decir, tendríamos que guardar el resultado en otra lista o imprimirlo porque si no se perdería.
# Con la función extend: shopping.extend(otra_lista) -> modifica la lista original, en este caso shopping, para añadirle la otra. Si introducimos un elemento convertible a lista se transformará automáticamente.
# Modificar una lista
# Modificando por su índice
shopping[
    0
] = "Jugo"  # Cambiaríamos el elemento 0 de shopping anterior, que es Agua, por Jugo
# Modificando con troceado
shopping[1:4] = [
    "Tomate",
    "Pasta",
]  # Cambiaríamos los elementos del 1 al 4-1(3), es decir, ['Agua', 'Tomate','Pasta', 'Atún']
# Borrar elementos
# Por su índice -> del shopping[3]
# Por su valor -> shopping.remove('Sal)
# Por su índice (con extracción) -> shopping.pop(2) si no se le indica índice se extrae el último elemento
# Por troceado -> shopping[1:4]=[]
# Borrado completo
# shopping.clear() -> borrado in-situ de memoria
# shopping = [] -> Nueva zona de memoria
# Encontrar un elemento: usamos shopping.index(elemento), a diferencia de los strings, las listas no tienen find pero si index
# Pertenencia de un elemento: como en los strings podemos comprobar si un elemento pertenece a una lista con el operador in
# Numero de ocurrencias: al igual que en los strings podmeos contar cuantas veces aparece un elemento en una lista
# Convertir lista a string: de la forma "sep".join(shopping) podemos transformar shopping a string usando sep como separador entre los diferentes elementos, si queremos poner un espacio de separador sería: " ".join(shopping)
# Ordenar una lista: ambos métodos admiten un parámetro "booleano" reverse
# Conservando la lista original-> sorted(shopping, reverse=True) el valor por defecto de reverse es False, es decir, si no lo ponemos la lista se ordenará de menor a mayor y alfabéticamente mientras que si es True se ordenará al revés
# Modificando la lista orginal-> shopping.sort(reverse=True) lo mismo que con sorted
# Longitud de una lista: len(shopping)
# Iterar sobre una lista: lo mismo que con string
# Iterar usando enumeración:
for i, product in enumerate(
    shopping,
    1,  # Con el 1 indicamos que en vez de empezar por 0 que es el valor por defecto empezamos en 1
):  # Lo que realmente estamos haciendo es crear un objeto iterable especial formado por tuplas las cuales tienen el número del índice que les corresponde a la izquierda y el elemento base a la derecha
    print(i, product)
# Iterar sobre múltiples listas a la vez:
shopping = ["Agua", "Aceite", "Arroz"]
details = ["mineral natural", "de oliva virgen", "basmati"]
for product, detail in zip(
    shopping, details
):  # zip produce un iterador de tuplas en las que la primera posición de cada tupla es el elemento del índice correspondiente en la primera lista y la segunda posición el correspondiente en la segunda lista
    print(product, detail)
# Copias: si asignamos una lista(nombre de variable) a otro nombre de variable no estaremos copiando la lista sino que estaremos enlazando la lista a dos nombres de variables distintos, es decir, si por ejemplo hacemos shopping2=shopping y luego modificamos shopping2 también modificaríamos shopping y viceversa. Quedarían enlazados teniendo el mismo id() y por lo tanto siendo el mismo objeto en memoria
# Usando copy(): copy_shopping=shopping.copy()
# Usando troceado: copy_shopping= shopping[:]
# Listas por compresión: técnica para crear lista de forma más compacta de la siguiente forma: [<expression> for <value> in <iterable> if <condition>]
values = "32,45,11,87,20,48"
int_values = [
    int(value) for value in values.split(",") if value.startswith("4")
]  # Basicamente consiste en ir guardando en una lista los valores que toma una expresión en cada iteración al iterar un iterable concreto, además, en este caso estamos filtrando para que dichos valores recogidos solo sean los que empiezan por 4
# Anidamiento en compresiones:
svalues = values.split(",")
combinations = [f"{v1}x{v2}" for v1 in svalues for v2 in svalues]
# sys.argv: pasar un parámetro por linea de comandos, el sys.argv[0] es el nombre del programa
import sys

number = int(sys.argv[1])
tobase = int(sys.argv[2])
match tobase:
    case 2:
        result = f"{number:b}"
    case 8:
        result = f"{number:o}"
    case 16:
        result = f"{number:x}"
    case _:
        result = None
if result is None:
    print(f"Base {tobase} not implemented!")
else:
    print(result)
# Funciones matemáticas: hay funciones matemáticas que se pueden aplicar sobre listas como: sum() -> suma todos los elementos, min()-> extrae el elemento con el menor valor, max() lo mismo que min pero con el mayor valor
# Listas de listas: Cuando necesitemos crear agrupaciones dentro de un gran grupo, por ejemplo, dentro de una lista que representa una tabla queremos representar dentro filas y columnas, en ese caso podríamos hacer que las filas representen listas dentro de una gran lista y las columnas representen los índices dentro de dichas sublistas de la forma: tabla=[['f0,c0','f0,c1']['f1,c0','f1,c1']] Para acceder a la fila 1, columna 0 sería: tabla[1][0]  (también podríamos representarlo a la inversa)
