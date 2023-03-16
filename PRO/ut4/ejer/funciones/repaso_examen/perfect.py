# *****************
# NÚMEROS PERFECTOS
# *****************
def calculate_divisors(number:int)->list:
    return [i for i in range(1,number) if number % i == 0]
        
def is_perfect(n:int)->bool:
    return sum(calculate_divisors(n))==n

