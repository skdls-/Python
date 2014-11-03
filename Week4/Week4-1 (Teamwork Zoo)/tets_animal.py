import unittest
from animal import Animal

class TestAnimal(unittest.TestCase):

	def setUp(self):

		self.my_animal = Animal("cat", 2, "Cat", "female", 3, 10)

	def test_init(self):

		self.assertEqual(self.my_animal.species, "cat")
		self.assertEqual(self.my_animal.age, 2)
		self.assertEqual(self.my_animal.name, "Cat")
		self.assertEqual(self.my_animal.gender, "female")
		self.assertEqual(self.my_animal.weight, 3)
		self.assertEqual(self.my_animal.life_expactancy, 10)

if __name__ == '__main__':
	unittest.main()

