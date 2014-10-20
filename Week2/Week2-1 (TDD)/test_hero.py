import unittest
from hero import Hero
from entity import Entity


class TestHealth(unittest.TestCase):

    def setUp(self):
        self.bron_hero = Hero("Bron", 100, "DragonSlayer")

    def test_hero_init(self):
        self.assertEqual(self.bron_hero.name, "Bron")
        self.assertEqual(self.bron_hero.health, 100)
        self.assertEqual(self.bron_hero.nickname, "DragonSlayer")


if __name__ == '__main__':
    unittest.main()
