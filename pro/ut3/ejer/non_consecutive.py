"""
El objetivo es encontrar el primer número no consecutivo dentro de una lista de valores
numéricos enteros. Si todos los valores son consecutivos entonces el resultado es None.
"""


def run(values: list) -> int:
    target = None
    if len(values) > 0:
        consecutive = values[0]
    for value in values:
        if value != consecutive:
            target = value
            break
        consecutive += 1
    return target


if __name__ == "__main__":
    run([1, 2, 3, 4, 6, 7, 8])
