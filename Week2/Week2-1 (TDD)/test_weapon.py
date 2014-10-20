from weapon import Weapon
import unittest

class TestWeapon(unittest.TestCase):

	def setUp(self):
		self.my_weapon = Weapon("Axe", 20, 0.4)

	def test_init(self):
		self.assertEqual(self.my_weapon.type, "Axe")
		self.assertEqual(self.my_weapon.damage, 20)
		self.assertEqual(self.my_weapon.critical_strike_percent, 0.4)

	def test_value_error(self):
		with self.assertRaises(ValueError):
			self.weapon = Weapon("Axe", 20 , 4)

	def test_critical_hit(self):
		answers = []
		for i in range(1, 100):
			if self.my_weapon.critical_hit() == True:
				answers.append(1)
			else:
				answers.append(0)
		self.assertIn(1, answers)
		self.assertIn(0, answers)

if __name__ == '__main__':
	unittest.main()