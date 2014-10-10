from magic_square import matrixTranspose


def check_rows(row):
    for number in row:
        if number > 9 or number < 1:
            return False
    for i in range(0, 8):
        for j in range(i + 1, 9):
            if row[i] == row[j]:
                return False
    return True


def cubes_to_rows(sudoku):
    cube = []
    result = []
    for d in range(0, 3):
        for k in range(0, 3):
            for i in range(0 + 3 * d, 3 + 3 * d):
                for j in range(0 + 3 * k, 3 + 3 * k):
                    cube.append(sudoku[i][j])
            result.append(cube)
            cube = []
    return result


def sudoku_test(sudoku):
    for row in sudoku:
        if check_rows(row) == False:
            return False
    for col in matrixTranspose(sudoku):
        if check_rows(col) == False:
            return False
    for elem in cubes_to_rows(sudoku):
        if check_rows(elem) == False:
            return False
    return True


print (sudoku_test(([
    [4, 5, 2, 3, 8, 9, 7, 1, 6],
    [3, 8, 7, 4, 6, 1, 2, 9, 5],
    [6, 1, 9, 2, 5, 7, 3, 4, 8],
    [9, 3, 5, 1, 2, 6, 8, 7, 4],
    [7, 6, 4, 9, 3, 8, 5, 2, 1],
    [1, 2, 8, 5, 7, 4, 6, 3, 9],
    [5, 7, 1, 8, 9, 2, 4, 6, 3],
    [8, 9, 6, 7, 4, 3, 1, 5, 2],
    [2, 4, 3, 6, 1, 5, 9, 8, 7]
])))
