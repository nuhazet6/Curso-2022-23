# **********************
# SUMANDO SOLO POSITIVOS
# **********************


def run(numbers: list) -> int:
    sum_positive = sum([posit_numb for posit_numb in numbers if posit_numb > 0])
    return sum_positive


if __name__ == "__main__":
    run([1, -4, 7, 12])
