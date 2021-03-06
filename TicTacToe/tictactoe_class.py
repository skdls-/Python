from bonus_functions import *


class TicTacToe():

    def __init__(self, board):
        self.board = board
        self.AI_wins = 0
        self.my_wins = 0

    def print_my_board(self):
        print_board(self.board)

    def game_over(self):
        if win_by_diagonal(self.board) or win_by_col(self.board) or win_by_row(self.board):
            return True
        return False

    def place_x(self):
        row = 0
        col = 0
        position = input("Position: ")
        position = int(position)
        while int(position) > 9 or int(position) < 1:
            print("Add numbers only between 0 and 9")
            position = input("Position: ")
        else:
            if position == 1:
                row = 0
                col = 0
            elif position == 2:
                row = 0
                col = 1
            elif position == 3:
                row = 0
                col = 2
            elif position == 4:
                row = 1
                col = 0
            elif position == 5:
                row = 1
                col = 1
            elif position == 6:
                row = 1
                col = 2
            elif position == 7:
                row = 2
                col = 0
            elif position == 8:
                row = 2
                col = 1
            elif position == 9:
                row = 2
                col = 2
        if self.board[row][col] != "X" and self.board[row][col] != "O":
            self.board[row][col] = 'X'
        else:
            print ("Taken! Try again! ")
            self.place_x()

    def AI_place_random_O(self):
        if not has_free_spots(self.board):
            print ("Nobody wins!")
        elif has_free_corner(self.board):
            mark_free_corner_O(self.board)
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
# offensive part
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
        elif first_move_x_corner(self.board):
            self.board[1][1] = "O"
            return
        elif first_move_x_middle(self.board):
            self.board[0][0] = "O"
            return
        elif block_fork_try(self.board):
            self.board[1][0] = "O"
            return
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
        if not self.game_over() and not has_free_spots(self.board):
            print ("Nobody Wins!")
            self.print_my_board()
        while not self.game_over() and has_free_spots(self.board):
            self.print_my_board()
            self.place_x()
            if self.game_over():
                print ("You win!")
                self.my_wins += 1
            else:
                self.AI_place_O()
                if self.game_over():
                    print ("Hah, looser! :)")
                    self.AI_wins += 1
        self.print_my_board()
        print ("---------------")
        print ("Your wins: ", self.my_wins)
        print ("Computer wins: ", self.AI_wins)
        print ("---------------")
        print (
            "Nice! One more time?\nPress Ctrl+C to exit if tired of playing!")
        self.board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.one_game()
