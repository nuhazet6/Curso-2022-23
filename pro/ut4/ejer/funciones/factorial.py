# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(n):
    if n < 0:
        return None
    result = 1
    for factor in range(2, n + 1):
        result *= factor
    return result
