import unittest
from orc import Orc
from entity import Entity
from weapon import Weapon


class Test_Orc(unittest.TestCase):

    def setUp(self):
        self.my_orc = Orc("Orcy", 100, 1.5)

    def test_orc_init(self):
        self.assertEqual(self.my_orc.name, "Orcy")
        self.assertEqual(self.my_orc.health, 100)
        self.assertEqual(self.my_orc.max_health, self.my_orc.health)

    def test_orc_attack_with_weapon(self):
    	self.proba = Weapon("Axe", 20, 0.5)
    	self.my_orc.equip_weapon(self.proba)
    	self.assertEqual(self.my_orc.attack(), 30)

    def test_orc_attack_without_weapon(self):
    	self.proba = None
    	self.my_orc.equip_weapon(self.proba)
    	self.assertEqual(self.my_orc.attack(), 0)



if __name__ == '__main__':
    unittest.main()
