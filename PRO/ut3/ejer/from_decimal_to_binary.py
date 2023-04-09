decimal = 25
binary_number = []
while decimal >= 1:
    remainder = decimal % 2
    binary_number.append(remainder)
    decimal //= 2
binary_number.reverse()
binary_number = [str(i) for i in binary_number]
binary_number = "".join(binary_number)
print(binary_number)
