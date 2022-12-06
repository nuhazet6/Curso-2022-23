# **************
# POTENCIAS DE 2
# **************


def run(num_powers: int) -> list:
    base = 2
    powers2 = [base**exponent for exponent in range(num_powers + 1)]
    return powers2


if __name__ == "__main__":
    run(0)
