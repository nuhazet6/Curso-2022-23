# *******************************
# DECORANDO CON VALORES ABSOLUTOS
# *******************************
def fabs(func):
    def wrapper(*args, **kwargs):
        result = func(*args,**kwargs)
        return abs(result)
    return wrapper

@fabs
def fprod(a,b):
    return a*b    
