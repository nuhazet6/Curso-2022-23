# *********************************
# ELEMENTOS DUPLICADOS CONSECUTIVOS
# *********************************


def run(items: list) -> list:
    result = []
    last_item = None
    for item in items:
        if item != last_item:
            result.append(item)
        last_item = item
    return result


if __name__ == "__main__":
    run([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])
