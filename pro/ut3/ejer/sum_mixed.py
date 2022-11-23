"""
Dada una lista de enteros y enteros como cadenas de texto, calcule la suma de todos los
valores de la lista como si todos sus elementos fueran números.
"""


def run(items: list) -> int:

    numbers = [int(i) for i in items]
    sum_items = sum(numbers)

    return sum_items
