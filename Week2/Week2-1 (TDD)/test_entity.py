import unittest
from entity import Entity
from orc import Orc
from weapon import Weapon



class Test_Entity(unittest.TestCase):

    def setUp(self):
        self.my_entity = Entity("Entity", 100)

    def test_init(self):
        self.assertEqual(self.my_entity.name, "Entity")
        self.assertEqual(self.my_entity.health, 100)
        self.assertEqual(self.my_entity.max_health, self.my_entity.health)

    def test_is_alive(self):
        self.assertTrue(self.my_entity.is_alive())

    def test_is_alive_2(self):
        self.my_entity.health = 0
        self.assertFalse(self.my_entity.is_alive())

    def test_take_damage(self):
        self.my_entity.take_damage(10)
        self.assertEqual(self.my_entity.health, 90)

    def test_take_damage_more_than_hp(self):
        self.my_entity.take_damage(110)
        self.assertEqual(self.my_entity.get_health(), 0)

    def test_take_healing_dead_hero(self):
        self.my_entity.take_damage(120)
        self.assertFalse(self.my_entity.take_healing(10))

    def test_take_healing_more_than_max_hp(self):
        self.my_entity.take_damage(50)
        self.my_entity.take_healing(100)
        self.assertEqual(self.my_entity.health, 100)

    def test_take_healing_less_then_max_hp(self):
        self.my_entity.take_damage(50)
        self.my_entity.take_healing(10)
        self.assertEqual(self.my_entity.health, 60)

    def test_has_weapon(self):
    	self.proba = Weapon("axe", 20, 0.5)
    	self.my_entity.equip_weapon(self.proba)
    	self.assertTrue(self.my_entity.has_weapon())

if __name__ == '__main__':
    unittest.main()
