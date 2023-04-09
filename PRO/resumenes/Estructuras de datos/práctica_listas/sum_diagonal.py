# *****************************
# SUMA DE LA DIAGONAL PRINCIPAL
# *****************************


def run(matrix: list) -> int:
    sum_diagonal = sum(
        [
            matrix[v1][v2]
            for v1 in range(len(matrix))
            for v2 in range(len(matrix[v1]))
            if v1 == v2
        ]
    )
    return sum_diagonal


if __name__ == "__main__":
    run([[4, 6, 1], [2, 9, 3], [1, 7, 7]])
