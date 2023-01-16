min_ascii = 33
max_ascii = 127
output = ""
new_line = 1
for ascii_decimal in range(min_ascii, max_ascii + 1):
    char = chr(ascii_decimal)
    output += f"{ascii_decimal:03d} {char:s}   "
    if new_line % 5 == 0:
        output += "\n"
    new_line += 1
print(output)
