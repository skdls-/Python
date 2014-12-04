from tictactoe import *

def AI_place_random_O(board):
    row = randint(0, 2)
    col = randint(0, 2)
    if board[int(row)][int(col)] != "X" and board[int(row)][int(col)] != "O":
        board[int(row)][int(col)] = 'O'
    else:
        AI_place_random_O(board)


def AI_place_O(board):
    mapped = map_board(board)
    # returns a list of the rows witch have 2 X-es and the AI must counter them
    danger_rows = [row for row in mapped if has_two_x(row)]
    # returns a lsit of the petoential winning rows
    winning_rows = [row for row in mapped if has_two_o(row)]
    print (winning_rows)
    #if there are such rows
    if winning_rows != []:
        for row in board:
            if has_two_o(row):
                place_O_where_not_o(row)
                return
        board = rows_to_cols(board)
        print_board(board)
        for col in board:
            if has_two_o(col):
                place_O_where_not_o(col)
                print (board)
                print ("--------")
                board = rows_to_cols(board)
                return board
        diagonal1 = get_diagonal(board)
        diagonal2 = get_other_diagonal(board)
        diagonals = [diagonal1, diagonal2]
        for diag in diagonals:
            print (diagonals)
            if has_two_o(diag):
                place_O_where_not_o(diag)
                return
    elif danger_rows != []:
        for row in board:
            if has_two_x(row):
                place_O_where_not_x(row)
                return
        for col in rows_to_cols(board):
            if has_two_x(col):
                place_O_where_not_x(col)
                return
        diagonal1 = get_diagonal(board)
        diagonal2 = get_other_diagonal(board)
        diagonals = [diagonal1, diagonal2]
        for diag in diagonals:
            if has_two_x(diag):
                place_O_where_not_x(diag)
                return
    else:
        AI_place_random_O(board)

def one_game(board):
    while not game_over(board):
        print_board(board)
        place_x(board)
        board = AI_place_O(board)


one_game([["O", "2", "O"], ["4", "5", "6"], ["7", "8", "9"]])