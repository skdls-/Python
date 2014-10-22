import unittest
from hero import Hero
from orc import Orc
from weapon import Weapon
from entity import Entity
from fight import Fight


class TestFight(unittest.TestCase):

    def setUp(self):
        self.my_hero = Hero("Hero",  100, "Hero")
        self.my_orc = Orc("Orc", 100, 1.5)
        self.the_fight = Fight(self.my_hero, self.my_orc)

    def test_init(self):
        self.assertEqual(self.my_hero.name, "Hero")
        self.assertEqual(self.my_hero.health, 100)
        self.assertEqual(self.my_hero.nickname, "Hero")
        self.assertEqual(self.my_orc.name, "Orc")
        self.assertEqual(self.my_orc.health, 100)
        self.assertEqual(self.my_orc.berserk_factor, 1.5)

    def test_attacks_first(self):
        my_arr = []
        for i in range(0, 100):
            if self.the_fight.attacks_first() == True:
                my_arr.append(1)
            my_arr.append(0)
        self.assertIn(1, my_arr)
        self.assertIn(0, my_arr)

    def test_simulate_fight(self):
        proba1 = Weapon("axe", 1, 0.1)
        proba2 = Weapon("sword", 40, 0.9)
        self.my_hero.equip_weapon(proba1)
        self.my_orc.equip_weapon(proba2)
        the_fight = Fight(self.my_hero, self.my_orc)
        self.assertFalse(the_fight.simulate_fight())

    

if __name__ == '__main__':
    unittest.main()
