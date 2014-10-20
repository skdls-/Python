import unittest
from Count_Words import count_words


class count_words_test(unittest.TestCase):

    def test_empty_count_words(self):
        self.assertEqual({}, count_words([]))

    def test_count_words(self):
        self.assertEqual(count_words(['apple', 'banana', 'apple', 'pie']),
                         {'apple': 2, 'banana': 1, 'pie': 1})

    def test_increases_number(self):
        self.assertEqual(count_words(['apple', 'banana', 'apple', 'pie', 'apple']),
                         {'apple': 3, 'banana': 1, 'pie': 1})

    def test_missing_element(self):
    	self.assertFalse(count_words(['apple', 'banana', 'apple', 'pie', 'new_elem']) == {'apple': 2, 'banana': 1, 'pie': 1})


if __name__ == '__main__':
    unittest.main()
