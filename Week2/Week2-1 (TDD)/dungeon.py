from hero import Hero
from orc import Orc
from weapon import Weapon
from entity import Entity


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
                print("%c "%j, end='' )
        print ("\n")

    def spawn(self, player_name, entity):
        self.player_name = player_name
        self.entity = entity
        if type(entity) is Hero:
            for i in range(0, len(self.map_array)):
                for j in range(0, len(self.map_array[i])):
                    if "S" in self.map_array[i]:
                        self.map_array[i][j] = 'H'
                        self.entity.i_coord = i
                        self.entity.j_coord = j
                        self.players[player_name] = entity
                        return True
        elif type(entity) is Orc:
            for i in range(0, len(self.map_array)):
                for j in range(0, len(self.map_array[0])):
                    if "S" in self.map_array[i]:
                        self.map_array[i][j] = 'O'
                        self.entity.i_coord = i
                        self.entity.j_coord = j
                        self.players[player_name] = entity
                        return True
        else:
            return False

    """def move(self, player_name, direction):
        self.direction = direction
        if direction == "right":
            for i in range (0, len(self.map_array)):
                for j in range (0, len(self.map_array[i])-1):
                    if self.map_array[i][j+1] == '.' and self.map_array[i][j] == 'H' and self.map_array[i][j+1]:
                        self.map_array[i][j+1] = 'H'
                        self.map_array[i][j] = '.'
                        self.players[player_name].i_coord = i
                        self.players[player_name].j_coord = j+1
                        break """

    def move(self, player_name, direction):
        self.direction = direction
        if direction == "right":
            if self.map_array[self.players[player_name].i_coord][self.players[player_name].j_coord + 1] == '.'and self.map_array[self.players[player_name].i_coord][self.players[player_name].j_coord] == 'H':
                self.map_array[self.players[player_name].i_coord][self.players[player_name].j_coord + 1] = 'H'
                self.map_array[self.players[player_name].i_coord][self.players[player_name].j_coord] = '.'
                self.players[player_name].j_coord += 1



def main():
    map = Dungeon("dungeon_map")
    goshko = Hero("Hero", 100, "Hero")
    map.spawn("Goshko", goshko)
    map.print_map()
    map.move("Goshko", "right")
    map.print_map()
    print(map.players["Goshko"].i_coord, map.players["Goshko"].j_coord)



if __name__ == '__main__':
    main()
