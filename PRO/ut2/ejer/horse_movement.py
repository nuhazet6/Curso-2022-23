objective_x = 7
objective_y = 8
x_position = 0
y_position = 0
change_1 = 1
change_2 = 2
while x_position <= objective_x and y_position <= objective_y:
    print(f"({x_position}, {y_position})")
    x_position += change_1
    y_position += change_2
    aux = change_1
    change_1 = change_2
    change_2 = aux
    # change_1, change_2 = change2, change1

flow = True
objective_x = 7
objective_y = 8
x_position = 0
y_position = 0
while x_position <= objective_x and y_position <= objective_y:
    print(f"({x_position} , {y_position})")
    x_position += 2 - flow
    y_position += 1 + flow
    flow = not flow
