import unittest
from Count_unique_words import Count_unique_words


class Unique_Words_Test(unittest.TestCase):

    def test_empty_arr(self):
        self.assertEqual(0, Count_unique_words([]))

    def test_unique_words(self):
        self.assertEqual(
            3, Count_unique_words(['apple', 'banana', 'apple', 'pie']))

    def test_count_increasing(self):
        self.assertEqual(4, Count_unique_words(
            ['apple', 'banana', 'apple', 'pie', 'new_word', 'new_word', 'new_word', 'new_word']))

if __name__ == '__main__':
    unittest.main()
