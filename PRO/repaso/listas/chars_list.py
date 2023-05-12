# **********************
# DESPLEGANDO CARACTERES
# **********************


def run(texts: list) -> list:
    # TU CÓDIGO AQUÍ
    chars = []
    for element in texts:
        chars.extend(element)
    return chars


if __name__ == '__main__':
    run(['uno', 'dos', 'tres'])