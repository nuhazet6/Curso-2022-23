# *******************************
# DECORANDO CON VALORES ABSOLUTOS
# *******************************
def fabs(matr):
    def wrapper(*args: int) -> int:
        return abs(matr(*args))

    return wrapper


@fabs
def fprod(a: int, b: int) -> int:
    return a * b
