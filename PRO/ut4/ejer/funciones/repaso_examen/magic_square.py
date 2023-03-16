# ***************
# CUADRADO MÁGICO
# ***************
def sum_column(matrix:list,num_column:int)-> int:
    column = [row[num_column] for row in matrix]
    return sum(column)

def sum_main_diagonal(matrix:list):
    main_diagonal = [matrix[i][i]for i in range(len(matrix))]
    return sum(main_diagonal)

def sum_inverse_diagonal(matrix:list):
    inverse_diagonal = [matrix[i][j] for i,j in enumerate(range(len(matrix)-1,0-1,-1))]
    return sum(inverse_diagonal)

def is_magic_square(values:list):
    target_value = sum_main_diagonal(values)
    output = target_value == sum_inverse_diagonal(values)
    for i in range(len(values)):
        row_sum = sum(values[i])
        column_sum = sum_column(values,i)
        output = row_sum == target_value == column_sum
    return output
