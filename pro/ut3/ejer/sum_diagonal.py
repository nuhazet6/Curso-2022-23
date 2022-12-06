# *****************************
# SUMA DE LA DIAGONAL PRINCIPAL
# *****************************


def run(matrix: list) -> int:
    main_diagonal = [matrix[i][i] for i in range(len(matrix))]
    sum_diagonal = sum(main_diagonal)
    return sum_diagonal


if __name__ == "__main__":
    run([[4, 6, 1], [2, 9, 3], [1, 7, 7]])
