import unittest
from group_by import group_by
from group_by import is_even


class group_by_test(unittest.TestCase):

	def test_odds(self):
		self.assertEqual(group_by(is_even, [1,2,3,4,5,6,7,8]),
			{'even': [2, 4, 6, 8] , 'odd': [1, 3, 5, 7]})

	def test_more_odds(self):
		self.assertEqual(group_by(is_even, [1,2,3,4,5,6,7,8,11,13,15]),
			{'even': [2, 4, 6, 8] , 'odd': [1, 3, 5, 7, 11, 13, 15]})

	def test_another_group(self):
		self.assertNotEqual(group_by(is_even, [1,2,3,4,5,6,7,8,11,13,15]),
			{'even': [2, 4, 6, 8] , 'odd': [1, 3, 5, 7, 11, 13, 15], 'new_thing': [123,123]})

if __name__ == '__main__':
	unittest.main()