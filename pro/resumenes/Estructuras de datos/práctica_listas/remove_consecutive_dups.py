# *********************************
# ELEMENTOS DUPLICADOS CONSECUTIVOS
# *********************************


def run(items: list) -> list:
    result = [items[0]]
    for index_item in range(1, len(items)):
        item = items[index_item]
        last_item = items[index_item - 1]
        if item != last_item:
            result.append(item)
    return result


if __name__ == "__main__":
    run([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])
