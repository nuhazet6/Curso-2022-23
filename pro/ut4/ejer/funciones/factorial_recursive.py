# *******************************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO (CON RECURSIVIDAD)
# *******************************************************


def factorial(n: int) -> int:
    if n < 0:
        return None
    if n == 0:
        return 1
    return factorial(n - 1) * n
