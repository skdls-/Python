import unittest
from reduce_file_path_moe import reduce_file_path

class ReducePathTest(unittest.TestCase):

	def test_if_there_are_single_dots(self):
		self.assertNotIn(".", reduce_file_path("/home//////////////radorado/code/./hackbulgaria/week0/../../../."))

	def test_if_there_are_double_dots(self):
		self.assertNotIn("..", reduce_file_path("/home//////////////radorado/code/./hackbulgaria/week0/../../../."))

if __name__ == '__main__':
	unittest.main()