# Dada una lista de strings, obtenga otra lista que contenga todos los caracteres de cada
# uno de los strings de la lista de entrada.


def run(texts: list) -> list:
    # TU CÓDIGO AQUÍ
    chars = []
    for word in texts:
        chars.extend(word)
    return chars
