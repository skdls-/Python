from tictactoe import *


class TicTacToe():

    def __init__(self, board):
        self.board = board

    def print_my_board(self):
        print_board(self.board)

    def game_not_over(self):
        if win_by_diagonal(self.board) or win_by_col(self.board) or win_by_row(self.board):
            return False
        return True

    def place_x(self):
        row = input("Row: ")
        col = input("Col: ")
        if self.board[int(row)][int(col)] != "X" and self.board[int(row)][int(col)] != "O":
            self.board[int(row)][int(col)] = 'X'
        else:
            print ("Taken! Try again! ")
            self.place_x()

    def AI_place_random_O(self):
        if not has_free_spots(self.board):
            print ("Nobody wins!")
        else:
            row = randint(0, 2)
            col = randint(0, 2)
            if self.board[int(row)][int(col)] != "X" and self.board[int(row)][int(col)] != "O":
                self.board[int(row)][int(col)] = 'O'
            else:
                self.AI_place_random_O()

    def AI_place_O(self):
        mapped = map_board(self.board)
        # returns a list of the rows witch have 2 X-es and the AI must counter
        # them
        danger_rows = [row for row in mapped if has_two_x(row)]
        # returns a list of the potential winning rows
        winning_rows = [row for row in mapped if has_two_o(row)]
        # if there are such rows
#offensive part
        if winning_rows != []:
            for row in self.board:
                if has_two_o(row):
                    place_O_where_not_o(row)
                    return
            self.board = rows_to_cols(self.board)
            for col in self.board:
                if has_two_o(col):
                    place_O_where_not_o(col)
                    self.board = rows_to_cols(self.board)
                    return
            self.board = rows_to_cols(self.board)
            diagonal1 = get_diagonal(self.board)
            if has_two_o(diagonal1):
                index = where_is_no_o(diagonal1)
                if index == 1:
                    self.board[1][1] = 'O'
                elif index == 0:
                    self.board[0][0] = 'O'
                elif index == 2:
                    self.board[2][2] = 'O'
                return
            diagonal2 = get_other_diagonal(self.board)
            if has_two_o(diagonal2):
                index = where_is_no_o(diagonal2)
                if index == 1:
                    self.board[1][1] = "O"
                elif index == 0:
                    self.board[0][2] = 'O'
                elif index == 2:
                    self.board[2][0] = 'O'
                return
# defending part
        elif danger_rows != []:
            for row in self.board:
                if has_two_x(row):
                    place_O_where_not_x(row)
                    return
            self.board = rows_to_cols(self.board)
            for col in self.board:
                if has_two_x(col):
                    place_O_where_not_x(col)
                    self.board = rows_to_cols(self.board)
                    return
            self.board = rows_to_cols(self.board)
            diagonal1 = get_diagonal(self.board)
            if has_two_x(diagonal1):
                index = where_is_no_x(diagonal1)
                if index == 1:
                    self.board[1][1] = 'O'
                elif index == 0:
                    self.board[0][0] = 'O'
                elif index == 2:
                    self.board[2][2] = 'O'
                return
            diagonal2 = get_other_diagonal(self.board)
            if has_two_x(diagonal2):
                index = where_is_no_x(diagonal2)
                if index == 1:
                    self.board[1][1] = 'O'
                elif index == 0:
                    self.board[0][2] = 'O'
                elif index == 2:
                    self.board[2][0] = 'O'
                return
        else:
            self.AI_place_random_O()

    def one_game(self):
        while self.game_not_over():
            self.print_my_board()
            self.place_x()
            if self.game_not_over():
                self.AI_place_O()
                if not self.game_not_over():
                    print ("Winner is the: O")
                    self.print_my_board()                  
            else:
                print ("Winner is the: X")
                self.print_my_board()

tictac = TicTacToe([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])
tictac.one_game()

