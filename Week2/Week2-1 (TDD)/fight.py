from hero import Hero
from orc import Orc
from weapon import Weapon
from entity import Entity
from random import randint


class Fight(object):

    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def attacks_first(self):
        my_rand = randint(0, 100)
        if my_rand < 50:
            return True  # the Hero attacks first
        return False  # the Orc attacks first

    def simulate_fight(self):
        while self.hero.is_alive() and self.orc.is_alive():
            self.hero.take_damage(self.orc.attack())
            self.orc.take_damage(self.hero.attack())
            print ("Hero health: ", self.hero.health)
            print ("Orc health: ", self.orc.health)
        if self.hero.is_alive() and self.orc.is_alive() == False:
            print ("the Hero Won!")
            return True
        else:
            print ("the Orc Won!")
            return False
