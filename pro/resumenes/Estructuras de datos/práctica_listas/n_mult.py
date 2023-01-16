# ********************
# CALCULANDO MÚLTIPLOS
# ********************


def run(x: int, n: int) -> list:
    multiples = [value * x for value in range(1, n + 1)]
    return multiples


if __name__ == "__main__":
    run(1, 10)
