# ***************
# MEZCLA ORDENADA
# ***************


def run(values1: list, values2: list) -> list:
    total_values = values1 + values2
    merged = []
    for i in total_values:
        if i not in merged:
            j = 0
            for j in range(len(merged)):
                if i < merged[j]:
                    break
            else:
                j = len(merged)
            merged.insert(j, i)

    return merged


if __name__ == "__main__":
    run([1, 2, 3, 4], [1, 1, 2, 3, 4, 5])
