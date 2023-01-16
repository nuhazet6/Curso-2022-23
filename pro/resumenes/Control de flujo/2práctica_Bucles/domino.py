DOMINO_SIZE = 6
output = ""
for blue in range(DOMINO_SIZE + 1):
    for red in range(blue, DOMINO_SIZE + 1):
        output += f"{blue}|{red} "
    output += "\n"
print(output)
