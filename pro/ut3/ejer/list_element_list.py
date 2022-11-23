entr = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
output = []
for element in entr:
    if type(element) == list:
        output.extend(element)
    else:
        output.append(element)
print(output)
