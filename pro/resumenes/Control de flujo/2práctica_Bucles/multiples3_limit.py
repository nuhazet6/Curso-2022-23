input = 45
sum = 0
result = "0, "
while (sum := sum + 3) < input:
    result += f"{sum}, "
print(result[:-2])
