objetivo_x = 7
objetivo_y = 8
output = ""
x = 0
y = 0
flow = True
while x <= objetivo_x and y <= objetivo_y:
    output += f"({x},{y}) "
    x += 2 - flow
    y += 1 + flow
    flow = not flow
print(output)
