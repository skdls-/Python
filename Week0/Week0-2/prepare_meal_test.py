import unittest
from prepare_meal_number import prepare_meal
from random import randint


class prepare_meal_test(unittest.TestCase):

    def test_divisible_by_three(self):
        divisible_by_three = randint(1, 100) * 3
        self.assertIn('spam', prepare_meal(divisible_by_three))

    def test_divisible_by_five(self):
        divisible_by_five = randint(1, 100) * 5
        self.assertIn('and eggs', prepare_meal(divisible_by_five))

    def test_not_divisible_by_three(self):
        rand = 0
        while rand % 3 == 0:
            rand = randint(1, 100)
        self.assertNotIn('spam', prepare_meal(rand))

    def test_not_divisible_by_five(self):
        rand = 0
        while rand % 5 == 0:
            rand = randint(1, 100)
        self.assertNotIn('and eggs', prepare_meal(rand))


if __name__ == '__main__':
    unittest.main()
