INITIAL_CHAR = 33
FINAL_CHAR = 127
COLUMN_AMOUNT = 5
output = ""
num_chars = 1
for char in range(INITIAL_CHAR, FINAL_CHAR + 1):
    output += f"{char:03d} {chr(char)}   "
    if num_chars % COLUMN_AMOUNT == 0:
        output += "\n"
    num_chars += 1
print(output)
