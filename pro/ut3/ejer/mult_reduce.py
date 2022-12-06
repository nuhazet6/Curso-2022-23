# ************************
# MULTIPLICACIÓN EN CADENA
# ************************


def run(numbers: list) -> int:
    rmult = 1
    for factor in numbers:
        rmult *= factor
    return rmult


if __name__ == "__main__":
    run([1, 2, 3, 4])
