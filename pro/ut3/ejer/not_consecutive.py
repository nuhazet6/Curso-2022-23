entr = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
output = []
last_i = None
for i in entr:
    if i != last_i:
        output.append(i)
    last_i = i
print(output)
