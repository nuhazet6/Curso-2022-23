DOMINO_MAX = 6
for left in range(DOMINO_MAX + 1):
    line = ""
    for right in range(left, DOMINO_MAX + 1):
        line += f"{left}|{right} "
    print(line)
