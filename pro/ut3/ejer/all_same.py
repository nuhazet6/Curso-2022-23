# *****************************
# SOMOS IGUALES, PERO DISTINTOS
# *****************************


def run(items: list) -> bool:
    for item in items:
        if item != items[0]:
            all_same = False
            break
    else:
        all_same = True
    return all_same


if __name__ == "__main__":
    run([1, 1, 1, 1, 1, 1])
