# *****************
# DECIMAL A BINARIO
# *****************


def run(num: int) -> str:
    invert_bin = []
    while num >= 1:
        invert_bin.append(str(num % 2))
        num //= 2
    to_bin = "".join(reversed(invert_bin))
    return to_bin


if __name__ == "__main__":
    run(1)
