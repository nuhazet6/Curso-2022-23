# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(n):
    result = 1
    for factor in range(2, n + 1):
        result *= factor
    return result
