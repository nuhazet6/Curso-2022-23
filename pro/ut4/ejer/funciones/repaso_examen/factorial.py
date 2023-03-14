# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(n:int):
    if n < 0:
        return None
    result = 1
    for i in range(2,n + 1):
        result *= i
    return result

