def matrixTranspose(matrix):
    result = []
    column = []
    for i in range(0, int(len(matrix[0]))):
        for j in range(0, int(len(matrix))):
            column.append(matrix[j][i])
        result.append(column)
        column = []
    return result


def check_diagonals(matrix):
    diag1 = 0
    diag2 = 0
    for i in range(0, int(len(matrix))):
        k = i
        diag1 += matrix[i][k]
    for j in range(0, int(len(matrix))):
        z = int(len(matrix)) - j - 1
        diag2 += matrixTranspose(matrix)[j][z]
    if diag1 == diag2:
        return True
    return False


#print (check_diagonals([[2, 2, 9], [1, 9, 3], [9, 3, 16]]))


def magic_square(matrix):
    i = 0
    sum_rows = 0
    sum_cols = 0
    for j in range(0, int(len(matrix))):
        if sum(matrix[i]) != sum(matrix[j]):
            return False
    sum_rows = sum(matrix[0])
    for k in range(0, int(len(matrix))):
        if sum(matrixTranspose(matrix)[i]) != sum(matrixTranspose(matrix)[k]):
            return False
    sum_cols = sum(matrixTranspose(matrix)[0])
    print (sum_cols)
    print (sum_rows)
    diag1 = 0
    diag2 = 0
    for i in range(0, int(len(matrix))):
        k = i
        diag1 += matrix[i][k]
    for j in range(0, int(len(matrix))):
        z = int(len(matrix)) - j - 1
        diag2 += matrixTranspose(matrix)[j][z]
    print (diag1)
    print (diag2)
    if (sum_cols == sum_rows and diag1 == diag2 and diag1 == sum_cols):
        return True
