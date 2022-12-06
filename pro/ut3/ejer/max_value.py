# ************
# VALOR MÁXIMO
# ************


def run(values: list) -> int:
    max_value = values[0]
    for number in values:
        if number > max_value:
            max_value = number
    return max_value


if __name__ == "__main__":
    run([-11, 10, -6, 15, -1])
