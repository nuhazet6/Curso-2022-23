# *********************
# ORDENE MI DICCIONARIO
# *********************


def run(unsorted_items: dict) -> list:
    # TU CÓDIGO AQUÍ
    sorted_items = sorted(unsorted_items.items(), key=lambda t: t[1])

    return sorted_items


if __name__ == "__main__":
    run({"a": "two", "b": "one", "c": "three"})
