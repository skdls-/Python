from bonus_functions import *
import unittest


class TestTicTacFuncs(unittest.TestCase):

    def test_all_same(self):

        self.assertTrue(all_same([1, 1, 1]))
        self.assertFalse(all_same([1, 2, 3]))

    def test_get_col(self):

        self.assertEqual(get_col([[1, 2], [3, 4]], 0), [1, 3])

    def test_rows_to_cols(self):

        self.assertEqual(rows_to_cols([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [
                         [1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_win_by_row(self):

        self.assertTrue(
            win_by_row([["1", "2", "3"], ["X", "X", "X"], ["7", "8", "9"]]))

    def test_win_by_col(self):

        self.assertTrue(
            win_by_col([["X", "2", "3"], ["X", "5", "6"], ["X", "8", "9"]]))

    def test_get_diagonal(self):

        self.assertEqual(get_diagonal(
            [["X", "2", "3"], ["X", "5", "6"], ["X", "8", "9"]]), ["X", "5", "9"])

    def test_get_other_diagonal(self):

        self.assertEqual(get_other_diagonal(
            [["X", "2", "3"], ["X", "5", "6"], ["X", "8", "9"]]), ["3", "5", "X"])

    def test_has_two_x(self):

        self.assertTrue(has_two_x(["X", "X", "3"]))

    def test_has_two_o(self):

        self.assertTrue(has_two_o(["O", "O", "3"]))


if __name__ == '__main__':
    unittest.main()
