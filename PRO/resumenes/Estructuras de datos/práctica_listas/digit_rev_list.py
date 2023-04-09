# ************************
# DÍGITOS EN ORDEN INVERSO
# ************************


def run(number: int) -> list:
    rev_digits = []
    while number >= 1:
        rev_digits.append(number % 10)
        number //= 10
    return rev_digits


if __name__ == "__main__":
    run(35231)
