from entity import Entity


class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.set_berserk_factor(berserk_factor)
        self.max_health = health

    def set_berserk_factor(self, berserk_factor):
        if berserk_factor > 2:
            self.berserk_factor = 2
        elif berserk_factor < 1:
            self.berserk_factor = 1
        else:
            self.berserk_factor = berserk_factor

    def attack(self):
    	if self.weapon == None:
    		return 0
    	return self.weapon.damage * self.berserk_factor

