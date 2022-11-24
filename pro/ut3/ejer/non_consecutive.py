"""
El objetivo es encontrar el primer número no consecutivo dentro de una lista de valores
numéricos enteros. Si todos los valores son consecutivos entonces el resultado es None.
"""


def run(values: list) -> int:
    target = None
    if len(values) > 0:
        next_number = values[0]
    for i in range(len(values)):
        if values[i] != next_number:
            target = values[i]
            break
        next_number = values[i] + 1

    return target


if __name__ == "__main__":
    run([1, 2, 3, 4, 6, 7, 8])
