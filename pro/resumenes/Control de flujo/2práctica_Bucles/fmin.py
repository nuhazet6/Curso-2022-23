min = -9
max = 9
smaller_y = min**2 - 6 * min + 3
smaller_x = min
for x in range(min + 1, max + 1):
    y = x**2 - 6 * x + 3
    if y < smaller_y:
        smaller_y = y
        smaller_x = x
print(smaller_y, smaller_x)
