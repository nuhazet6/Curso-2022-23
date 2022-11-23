matrix = [[4, 6, 1], [2, 9, 3], [1, 7, 7]]
sum_diagonal = 0
for i in range(len(matrix)):
    sum_diagonal += matrix[i][i]
print(sum_diagonal)

# lista pro compresion

main_diagonal = [matrix[i][i] for i in range(len(matrix))]
sum_diagonal = sum(main_diagonal)
print(sum_diagonal)
