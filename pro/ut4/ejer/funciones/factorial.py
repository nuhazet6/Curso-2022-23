# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(n):
    res = 1
    for n in range(n, 0, -1):
        res *= n
    return res
