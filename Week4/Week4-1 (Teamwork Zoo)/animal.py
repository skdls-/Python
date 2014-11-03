from random import randint


class Animal:

    def __init__(self, species, age, name, gender, weight, life_expactancy):

        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self.life_expactancy = life_expactancy

    def grow(self, years):

        self.age += years

    def eat(self, weight):

        self.weight += weight

    def dead(self):

        chance_of_dying = self.age / self.life_expactancy
        random_int = randint(1, self.life_expactancy)
        if random_int < chance_of_dying:
            return True
        return False
