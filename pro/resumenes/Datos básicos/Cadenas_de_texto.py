"Hola Mundo"  # Creando un string
'Si queremos "resaltar" una palabra podemos usar "comillas dobles"'  # Se pueden usar comillas simples en string construidos con comillas dobles o viceversa.
"También se 'pueden' usar \"escape\""  # El escape es usar la barra invertida antes de poner un carácter especial
"""Los textos pueden alargarse mucho
tanto que a lo mejor necesitamos varias lineas
en ese caso, se pueden usar comillas triples
"""
""  # Cadena vacía: es un string sin carácteres dentro
str(True)  # Resultado: "True", con str() convertimos otros datos en String
int("10")
# Resultado: 10 , ya lo hemos visto pero con int()podríamos convertir los Strings ademas, de los floats u otro tipo de dato compatible
int("FF", 16)
# Resultado: 255 si le pasamos la base que queremos convertir al int() podremos convertir más cosas
print("Salto de línea\nTabulador\tBarra invertida\\")
print(r"abc\ndef")
# Cadena raw data, no tiene en cuenta el escape de la barra invertida
saludo1 = "Hola"
saludo2 = "Buenas"
print(saludo1, saludo2, sep=", ", end="y Adiós\n")
# Hay parámetros dentro del print para modificar el separador(sep='') entre variables introducidas(el separador por defecto es el espacio) y el final(end='') del propio print (el final predeterminado es \n)
name = input("Introduzca su nombre: ")
# Podemos pedir datos por teclado con input(), siempre nos devolverá datos tipo str
saludo_personalizado = saludo1 + " " + name
# Usando el operador + podemos concatenar varios strings para formar uno solo
print(saludo_personalizado)
saludo1 * 3  # Resultado: HolaHolaHola El operador * en los string repite x veces los strings que queramos
saludo1[0]
# Resultado: H podemos coger un carácter concreto dentro de un String con los corchetes [] El índice va desde 0, representando el 0, el primer carácter del String, hasta el número de caracteres del String - 1, también podemos utilizar un índice negativo que va desde el -1, que sería el último elemento del String, hasta el -tamaño del String, que sería el primer elemento
saludo2[:-2]
# Resultado: Buen si al corchete le ponemos dos puntos, entonces estaremos realizando un troceado, existiendo varios tipos: [:]copia de todo el string, [start:] coge desde start hasta el final, [:end]coge desde el comienzo hasta end menos 1, [start:end] Extrae desde start hasta end menos 1, [start:end:step] lo mismo que el anterior solo que haciendo saltos de tamaño step
len(saludo2)  # Longitud de la cadena saludo2, en este caso daría 6
"Buen" in saludo2  # Comprobar si una subcadena, en este caso "Buen" forma parte de otra cadena, en este caso saludo2, el resultado aquí sería True. También se podría comprobar si no está con la negación de in, es decir, con not in
serial_number = "\n\t    \n   435234562344234   \n\n\t  "
serial_number.strip()  # Con strip podemos quitar por delante y por detras los caracteres que queramos, en este caso, como es el strip por defecto quitará todos los espacios, tabuladores(\t), saltos de línea(\n),etc
saludo2.startswith("Buen")  # Comprobar si una cadena empieza por alguna subcadena
saludo1.endswith("a")  # Comprobar si una cadena termina por una subcadena
saludo1.find(
    "ola"
)  # Se utiliza para buscar una subcadena en un String, si la encuentra devuelve el índice donde está la primera ocurrencia, si no, devuelve un -1
saludo1.index(
    "ola"
)  # Es igual que el find con la diferencia de que si no encuentra la subcadena devuelve una excepción
serial_number.count(
    "34"
)  # Cuenta la cantidad de veces que aparece una subcadena en una cadena
saludo2.replace("a", "o")
# Mayúsculas y minúsculas: .capitalize() cambia la primera letra del String por una mayúscula, .title() cambia la primera letra de cada palabra por mayúscula, .upper() cambia todo por mayúsculas, .lower() cambia todo por minúsculas, .swapcase() cambia minúsculas por mayúsculas y viceversa.
# Identificando caracteres: 'C3-PO'.isalnum() en este caso devolvería False, se encarga de devolver un booleano en función de sí el String solo contiene caracteres alfanuméricos o no, '314'.isnumeric() devolvería True, lo mismo que el anterior pero con caracteres numéricos, 'a-b-c'.isalpha() lo mismo pero con caracteres alfabéticos
# F-STRINGS f'Texto{variable} más texto{decimal:010.02f}' tipos de datos: :b -> binary :o -> octal :x -> hexadecimal :f -> decimal :e -> notación científica     ; f'{columna_izquierda:<s}|{columna_central^11s}|{columna_derecha>7s}' se pueden usar las flechas <>^ para alinear el contenido a la izquierda, derecha o al centro.
rocket_code = 0x1F680
rocket = chr(rocket_code)
print(
    rocket
)  # Con chr() podemos a partir de un numero en hexadecimal obtener el caracter unicode que represente dicho número
hex(ord(rocket))  # Con ord() obtenemos el código (en decimal) de un caracter unicode
