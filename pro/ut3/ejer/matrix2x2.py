A = [[6, 4], [8, 9]]
B = [[3, 2], [1, 7]]
item00 = A[0][0] * B[0][0] + A[0][1] * B[1][0]
item10 = A[0][0] * B[0][1] + A[0][1] * B[1][1]
item01 = A[1][0] * B[0][0] + A[1][1] * B[1][0]
item11 = A[1][0] * B[0][1] + A[1][1] * B[1][1]
result = [[item00, item10], [item01, item11]]
print(result)
A = [[6, 4, 3], [8, 9, 3], [4, 3, 1]]
B = [[3, 2, 1], [7, 1, 7], [6, 3, 1]]
# resultado = 64 25 37 \n 105 34 74 \n 39 14 26
output = ""
for row_A in range(len(A)):
    for column_B in range(len(B[0])):
        item = 0
        for row_B in range(len(B)):
            item += A[row_A][row_B] * B[row_B][column_B]
        output += f"{item:} "
    output += "\n"
print(output)

print("---")
A = [[6, 4], [8, 9], [4, 3]]
B = [[3, 2, 1], [7, 1, 7]]
# Resultado = 46 16 34 \n 87 25 71 \n 33 11 25
output = ""
for row_A in range(len(A)):
    for column_B in range(len(B[0])):
        item = 0
        for row_B in range(len(B)):
            item += A[row_A][row_B] * B[row_B][column_B]
        output += str(item) + " "
    output += "\n"
print(output)

print("---")
A = [[5, 4, 2], [1, 5, 3]]
B = [[8, 4], [2, 7], [4, 1]]
# Resultado = 56 50 \n 30 42
output = []
for row_A in range(len(A)):
    output.append([])
    for column_B in range(len(B[0])):
        item = 0
        for row_B in range(len(B)):
            item += A[row_A][row_B] * B[row_B][column_B]
        output[row_A].append(item)
print(output)
