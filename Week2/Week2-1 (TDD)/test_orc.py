import unittest
from orc import Orc
from entity import Entity


class Test_Orc(unittest.TestCase):

    def setUp(self):
        self.my_orc = Orc("Orcy", 100, 1.5)

    def test_orc_init(self):
        self.assertEqual(self.my_orc.name, "Orcy")
        self.assertEqual(self.my_orc.health, 100)
        self.assertEqual(self.my_orc.max_health, self.my_orc.health)


if __name__ == '__main__':
    unittest.main()
