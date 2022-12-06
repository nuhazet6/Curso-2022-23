# **************
# SUMA INVERTIDA
# **************


def run(numbers: list) -> int:
    add_inv = sum([inv_number * -1 for inv_number in numbers])
    return add_inv


if __name__ == "__main__":
    run([1, 2, 3, 4, 5])
