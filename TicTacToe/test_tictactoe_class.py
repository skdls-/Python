import unittest
from bonus_functions import *
from tictactoe_class import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def setUp(self):

        self.tictactoe1 = TicTacToe(
            [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])

    def test_init(self):

        self.assertEqual(
            [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]], self.tictactoe1.board)
        self.assertEqual(self.tictactoe1.my_wins, 0)
        self.assertEqual(self.tictactoe1.AI_wins, 0)

    def test_game_over(self):

        # by_row
        self.assertFalse(self.tictactoe1.game_over())
        self.tictactoe1.board = [
            ["X", "X", "X"], ["4", "5", "6"], ["7", "8", "9"]]
        self.assertTrue(self.tictactoe1.game_over())
        # by_col
        self.tictactoe1.board = [
            ["X", "2", "3"], ["X", "5", "6"], ["X", "8", "9"]]
        self.assertTrue(self.tictactoe1.game_over())
        # by main diagonal
        self.tictactoe1.board = [
            ["X", "2", "3"], ["4", "X", "6"], ["7", "8", "X"]]
        self.assertTrue(self.tictactoe1.game_over())
        # by secondary diagonal
        self.tictactoe1.board = [
            ["1", "2", "X"], ["4", "X", "6"], ["X", "8", "9"]]
        self.assertTrue(self.tictactoe1.game_over())

    def test_place_x(self):

        print ("Enter a position to check if it really writes something.")
        print ("Must be and integer between 1 and 9")
        self.tictactoe1.place_x()
        self.assertTrue(has_one_x(self.tictactoe1.board))

    def test_AI_place_random(self):

        self.tictactoe1.AI_place_random_O()
        self.assertTrue(has_one_o(self.tictactoe1.board))

    def test_AI_place_O_offensive_part(self):

        # check offensive part by row
        self.tictactoe1.board = [
            ["O", "O", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.tictactoe1.AI_place_O()
        self.assertTrue(self.tictactoe1.game_over())

        # check offensive part by col
        self.tictactoe1.board = [
            ["O", "2", "3"], ["O", "5", "6"], ["7", "8", "9"]]
        self.tictactoe1.AI_place_O()
        self.assertTrue(self.tictactoe1.game_over())

        # check offensive part by main diagonal
        self.tictactoe1.board = [
            ["O", "2", "3"], ["4", "O", "6"], ["7", "8", "9"]]
        self.tictactoe1.AI_place_O()
        self.assertTrue(self.tictactoe1.game_over())

        # check offensive part by secondary diagonal
        self.tictactoe1.board = [
            ["1", "2", "O"], ["4", "O", "6"], ["7", "8", "9"]]
        self.tictactoe1.AI_place_O()
        self.assertTrue(self.tictactoe1.game_over())

    def test_AI_fork_protections(self):

        # placing O in the middle, if first move is X-corner
        self.tictactoe1.board = [
            ["1", "2", "X"], ["4", "5", "6"], ["7", "8", "9"]]
        self.tictactoe1.AI_place_O()
        self.assertEqual(self.tictactoe1.board[1][1], "O")

    def test_AI_fork_prorections_part_2(self):

        # placing O at [1][0] if diagonal is [X,O,X]
        self.tictactoe1.board = [
            ["X", "2", "3"], ["4", "O", "6"], ["7", "8", "X"]]
        self.tictactoe1.AI_place_O()
        self.assertEqual(self.tictactoe1.board[1][0], "O")

    def test_AI_blocking_danger_rows(self):

        # placing O at rows if they have 2 X-es and an empty spot
        self.tictactoe1.board = [
            ["X", "X", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.tictactoe1.AI_place_O()
        self.assertEqual(self.tictactoe1.board[0][2], "O")

        # placing O at cols if they have 2 X-es and an empty spot
        self.tictactoe1.board = [
            ["X", "2", "3"], ["X", "5", "6"], ["7", "8", "9"]]
        self.tictactoe1.AI_place_O()
        self.assertEqual(self.tictactoe1.board[2][0], "O")

        # placing O at main diagonal if it has 2 X-es and an empty spot
        self.tictactoe1.board = [
            ["X", "2", "3"], ["4", "X", "6"], ["7", "8", "9"]]
        self.tictactoe1.AI_place_O()
        self.assertEqual(self.tictactoe1.board[2][2], "O")

        # placing O at secondary diagonal if it has 2 X-es and an empty spot
        self.tictactoe1.board = [
            ["1", "2", "X"], ["4", "X", "6"], ["7", "8", "9"]]
        self.tictactoe1.AI_place_O()
        self.assertEqual(self.tictactoe1.board[2][0], "O")


if __name__ == '__main__':
    unittest.main()
