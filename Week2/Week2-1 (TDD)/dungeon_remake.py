from hero import Hero
from orc import Orc
from weapon import Weapon
from entity import Entity
from fight import Fight


class Dungeon:

    def __init__(self, map):
        self.map = map
        self.dungeon_map = open(self.map)
        self.map_array = []
        for line in self.dungeon_map.readlines():
            self.map_array.append(list(line.strip()))
        self.dungeon_map.close()
        self.players = {}

    def print_map(self):
        for i in range(0, len(self.map_array)):
            print()
            for j in self.map_array[i]:
                print("%c " % j, end='')
        print ("\n")

    def spawn(self, player_name, entity):
        self.player_name = player_name
        self.entity = entity
        if type(entity) is Hero:
            for i in range(0, len(self.map_array)):
                for j in range(0, len(self.map_array[i])):
                    if self.map_array[i][j] == "S":
                        self.map_array[i][j] = 'H'
                        self.entity.i_coord = i
                        self.entity.j_coord = j
                        self.players[player_name] = entity
                        return True
        elif type(entity) is Orc:
            for i in range(0, len(self.map_array)):
                for j in range(0, len(self.map_array[0])):
                    if self.map_array[i][j] == "S":
                        self.map_array[i][j] = 'O'
                        self.entity.i_coord = i
                        self.entity.j_coord = j
                        self.players[player_name] = entity
                        return True
        else:
            return False

    def that_enemy(self, i_coord2, j_coord2):
        for i in self.players:
            if self.players[i].i_coord == i_coord2 and self.players[i].j_coord == j_coord2:
                return self.players[i]

    def move(self, player_name, direction):
        pyrva = self.players[player_name].i_coord
        vtora = self.players[player_name].j_coord
        self.direction = direction
        i = 0
        j = 0

        if direction == "right":
            i = 0
            j = 1
        elif direction == "left":
            i = 0
            j = -1
        elif direction == "down":
            i = 1
            j = 0
        elif direction == "up":
            i = -1
            j = 0

        if type(self.players[player_name]) == Hero and self.map_array[pyrva + i][vtora + j] == 'O':
            fight = Fight(
                self.players[player_name], self.that_enemy(pyrva + i, vtora + j))
            fight.simulate_fight()

        elif type(self.players[player_name]) == Orc and self.map_array[pyrva + i][vtora + j] == 'H':
            fight = Fight(
                self.players[player_name], self.that_enemy(pyrva + i, vtora + j))
            fight.simulate_fight()

        if self.map_array[pyrva + i][vtora + j] == '.':
            if type(self.players[player_name]) == Hero:
                self.map_array[pyrva + i][vtora + j] = 'H'
                self.map_array[pyrva][vtora] = '.'
                if direction == "left" or direction == "right":
                    self.players[player_name].j_coord += j
                else:
                    self.players[player_name].i_coord += i
            elif type(self.players[player_name]) == Orc:
                self.map_array[pyrva + i][vtora + j] = 'O'
                self.map_array[pyrva][vtora] = '.'
                if direction == "left" or direction == "right":
                    self.players[player_name].j_coord += j
                else:
                    self.players[player_name].i_coord += i
            else:
                return False

def game():
    map = Dungeon("dungeon_map")
    goshko = Hero("Hero", 100, "Hero")
    Orko = Orc("Orko", 100, 1.5)
    map.spawn("Goshko", goshko)
    map.spawn("Orko", Orko)
    map.print_map()
    while goshko.is_alive() and Orko.is_alive():
        move_hero = input("Move the hero! ")
        map.move("Goshko", move_hero)
        map.print_map()
        move_orc = input("Move the orc! ")
        map.move("Orko", move_orc)
        map.print_map()
    if not goshko.is_alive():
        print ("The Orc won!")
        return
    else:
        print ("The Hero won!")
        return


def main():
    game()
    map.print_map()

if __name__ == '__main__':
    main()
