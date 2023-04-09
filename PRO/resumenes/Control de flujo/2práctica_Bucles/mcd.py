a = 12
b = 44
if b < a:
    smaller = b
else:
    smaller = a
for divisor in range(smaller, 0, -1):
    module_a = a % divisor
    module_b = b % divisor
    is_divisor_a = module_a == 0
    is_divisor_b = module_b == 0
    if is_divisor_a and is_divisor_b:
        mcd = divisor
        break
