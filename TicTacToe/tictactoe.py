from random import randint

print("The computer plays with O-s")


def print_board(board):
    for i, row in enumerate(board):
        print (' '.join(row))


def all_same(items):
    return all(x == items[0] for x in items)


def get_col(matrix, num):
    result = []
    for row in matrix:
        result.append(row[num])
    return result


def rows_to_cols(board):
    result = []
    for i in range(0, 3):
        result.append(get_col(board, i))
    return result


def win_by_row(board):
    for row in board:
        if all_same(row):
            #print ("Winner is the: ", row[0])
            return True
    return False


def win_by_col(board):
    board_cols = rows_to_cols(board)
    return (win_by_row(board_cols))


def get_diagonal(board):
    diagonal = []
    i = 0
    for row in board:
        diagonal.append(row[i])
        i = i + 1
    return diagonal


def get_other_diagonal(board):
    other_diagonal = []
    i = 2
    for row in board:
        other_diagonal.append(row[i])
        i = i - 1
    return other_diagonal


def win_by_diagonal(board):
    diagonal1 = get_diagonal(board)
    diagonal2 = get_other_diagonal(board)
    diagonals = [diagonal1, diagonal2]
    return (win_by_row(diagonals))


'''def game_over(board):
    if win_by_diagonal(my_board) or win_by_col(my_board) or win_by_row(my_board):
        return True
    return False '''


def place_x(board):
    row = input("Row: ")
    col = input("Col: ")
    if board[int(row)][int(col)] != "X" and board[int(row)][int(col)] != "O":
        board[int(row)][int(col)] = 'X'
    else:
        place_x(board)


def map_board(board):
    result = []
    result.append(get_diagonal(board))
    result.append(get_other_diagonal(board))
    cols = rows_to_cols(board)
    for col in cols:
        result.append(col)
    for row in board:
        result.append(row)
    return result


def has_two_x(lst):
    count_o = 0
    count_x = 0
    for elem in lst:
        if elem == "X":
            count_x += 1
        elif elem == 'O':
            count_o += 1
    return count_x == 2 and count_o != 1


def has_two_o(lst):
    count_o = 0
    count_x = 0
    for elem in lst:
        if elem == "O":
            count_o += 1
        elif elem == "X":
            count_x += 1
    return count_o == 2 and count_x != 1


def place_O_where_not_o(lst):
    for elem in lst:
        if is_not_busy(lst, lst.index(elem)):
            lst[lst.index(elem)] = "O"
            return


def where_is_no_o(lst):
    for elem in lst:
        if is_not_busy(lst, lst.index(elem)):
            return lst.index(elem)


def where_is_no_x(lst):
    for elem in lst:
        if is_not_busy(lst, lst.index(elem)):
            return lst.index(elem)


def place_O_where_not_x(lst):
    for elem in lst:
        if is_not_busy(lst, lst.index(elem)):
            lst[lst.index(elem)] = "O"
            # break


def is_not_busy(lst, ind):
    return lst[ind] != "X" and lst[ind] != "O"


def has_free_spots(board):
    for row in board:
        for elem in row:
            if elem != "X" and elem != 'O':
                return True
    return False
