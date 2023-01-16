# *******************
# NO ERES CONSECUTIVO
# *******************


def run(values: list) -> int:
    target = None
    for value_index in range(1, len(values)):
        if values[value_index] != values[value_index - 1] + 1:
            target = values[value_index]
            break
    return target


if __name__ == "__main__":
    run([1, 2, 3, 4, 6, 7, 8])
