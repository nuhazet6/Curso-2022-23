# ******************
# POTENCIA RECURSIVA
# ******************


def power(x:int,n:int):
    if n==0:
        return 1
    return x*power(x,n-1)

