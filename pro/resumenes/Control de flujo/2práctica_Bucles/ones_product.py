STR_ONE = "1"
max_amount = 10
for ones_amount in range(1, max_amount):
    factor = int(STR_ONE * ones_amount)
    result = factor * factor
    operation_str = f"{factor} · {factor}"
    print(f"{operation_str:^{max_amount*2 +1}s} = {result:^{max_amount*2}d}")
