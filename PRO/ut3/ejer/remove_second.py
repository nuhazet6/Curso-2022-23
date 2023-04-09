"""
Dada una lista, genere otra lista eliminando el segundo elemento de forma repetida.
"""


def run(items: list) -> list:
    filter = []
    for i in range(0, len(items), 2):
        filter.append(items[i])

    # filter = [items[i] for i in range(0, len(items), 2)]

    # filter = items[::2]
    return filter
