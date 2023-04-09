# Tipos de datos: bool, int, float, complex, str, tuple, list, set, dict
# Reglas para variables: usar todo minúsculas para variables y todo mayúsculas para las constantes, no pueden empezar por un número, no pueden ser palabras reservadas del lenguaje, no pueden contener carácteres no permitidos, los permitidos son: letras(mayusculas o minúsculas), dígitos(sin empezar por estos), guiones bajos
# Reglas más avanzadas: usar sustantivos para variables, verbos para funciones y adjetivos para booleano, para booleanos también se puede usar "is_adjetivo" por ejemplo is_cold
tres = three = drei = 3
# Asignación multiple, consiste en asignar a varias variables el último valor que se indica, en este caso 3
print(
    tres
)  # Muestra el valor guardado en la variable tres, con la función print() muestras cosas dentro de los paréntesis
type(
    9
)  # Esto da int, type() sirve para mostrar el tipo del dato introducido dentro del paréntesis
isinstance(
    True, bool
)  # Esto daría True, la función isinstance comprueba que el primer parámetro introducido cumple el tipo de dato introducido como segundo parámetro.
# help()  # para obtener ayuda de lo que se introduce dentro de los paréntesis
# id()  # Para obtener el id del objeto (todos los tipos de datos son objetos en python)
# Operaciones: +, -, *, /, //, %, **. En orden: suma, resta, multiplicación, división con decimales, división entera, módulo, potencia
a = 2
b = a * 5  # Ejemplo operación asignándole el resultado a b
a += 1  # Asignación aumentada
abs(a - 10)  # Función para el valor absoluto daría: 7
a += False  # conversión implicita, al operar un booleano con un int en resultado es int
# Tipos de conversiones implícitas: bool + int = int; bool * float = float; int - float = float
int(
    3.4
)  # Esto daría 3, es una conversión explícita, es decir, indicamos el tipo de dato al que vamos a transformar.
# Transformaciones básicas de conversión: int() float() bool()
round(
    a / 3.1
)  # Redondear a 1 decimal, el decimal se puede cambiar, pudiendo redondear a 2, 3 o los decimales que sean.
# Bases: 0b, 0o, 0x respectivamente: binario, octal, hexadecimal
# Conversión de bases: bin(), oct(), hex() respectivamente: pasar a binario, pasar a octal, pasar a hexadecimal.
print(type(9), isinstance(False, bool), abs(a - 10 + False), int(3.4), round(a / 3.1))
