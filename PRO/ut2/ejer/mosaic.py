size = 10
for row in range(size):
    lane = ""
    for col in range(size):
        if row == col:
            lane += "X "
        elif row < col:
            lane += "U "
        else:
            lane += "D "
    print(lane)
