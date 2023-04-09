BASE = 2
upper_limit_exponent = int(
    input("Introduce un número para el máximo exponente de base 2 a calcular:")
)
powers_of_base = []
for exp in range(upper_limit_exponent + 1):
    powers_of_base.append(BASE**exp)
print(powers_of_base)

powers_of_base = [BASE**exp for exp in range(upper_limit_exponent + 1)]
print(powers_of_base)
