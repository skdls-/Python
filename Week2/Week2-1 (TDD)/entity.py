from weapon import Weapon


class Entity(object):

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = Weapon("Axe", 6, 0.5)
        self.i_coord = 0
        self.j_coord = 0

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, dmg_points):
        if dmg_points > self.health:
            self.health = 0
        else:
            self.health -= dmg_points

    def take_healing(self, healing_points):
        if self.is_alive() == False:
            return False
        elif healing_points + self.health > self.max_health:
            self.health = self.max_health
            return True
        else:
            self.health += healing_points
            return True

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def has_weapon(self):
        if self.weapon == None:
            return False
        return True

    def attack(self):
    	if self.weapon == None:
    		return 0
    	elif self.weapon.critical_hit() == True:
    		return self.weapon.damage * 2
    	else:
    		return self.weapon.damage
