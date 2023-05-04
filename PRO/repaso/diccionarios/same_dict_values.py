# ******************************
# VALORES IGUALES EN DICCIONARIO
# ******************************


def run(items: dict) -> bool:
    # TU CÓDIGO AQUÍ
    all_same = True
    buffer = list(items.values())
    buffer.append(None)
    buffer = buffer[0]
    for key in items:
        value = items[key]
        if buffer != value:
            all_same = False
            break
        buffer = value
    return all_same


if __name__ == '__main__':
    run({'a': 1, 'b': 1, 'c': 1, 'd': 1})