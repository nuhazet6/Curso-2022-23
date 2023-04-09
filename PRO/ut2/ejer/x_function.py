a = 1
b = 6
c = 3
dist = 9
i = dist
min_fun = a * i**2 - b * i + c
for i in range(-dist, dist):
    f_x = a * i**2 - b * i + c
    if f_x < min:
        min = f_x
        x = i
print(f"x = {x} f(x) = {min}")
