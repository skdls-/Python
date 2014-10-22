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

    def that_enemy(self, i_coord2, j_coord2):
        for i in self.players:
            if self.players[i].i_coord == i_coord2 and self.players[i].j_coord == j_coord2:
                return self.players[i] 

    def move(self, player_name, direction):
        pyrva = self.players[player_name].i_coord
        vtora = self.players[player_name].j_coord
        self.direction = direction

        if direction == "right":
            """if type(self.players[player_name]) == Hero and self.map_array[pyrva][vtora + 1] == 'O':
                fight = Fight(players[player_name], that_enemy(pyrva, vtora + 1))
            
            elif type(self.players[player_name]) == Orc and self.map_array[pyrva][vtora + 1] == 'H':
                fight = Fight(players[player_name], that_enemy(pyrva, vtora + 1)) """
            
            if self.map_array[pyrva][vtora + 1] == '.':
                if type(self.players[player_name]) == Hero:
                    self.map_array[pyrva][vtora + 1] = 'H'
                    self.map_array[pyrva][vtora] = '.'
                    self.players[player_name].j_coord += 1

                elif type(self.players[player_name]) == Orc:
                    self.map_array[pyrva][vtora + 1] = 'O'
                    self.map_array[pyrva][vtora] = '.'
                    self.players[player_name].j_coord += 1
            else:
                return False

        elif direction == "left":
            """if type(self.players[player_name]) == Hero and self.map_array[pyrva][vtora - 1] == 'O':
                fight = Fight(players[player_name], that_enemy(pyrva, vtora - 1))
            
            elif type(self.players[player_name]) == Orc and self.map_array[pyrva][vtora - 1] == 'H':
                fight = Fight(players[player_name], that_enemy(pyrva, vtora - 1)) """

            if self.map_array[pyrva][vtora - 1] == '.':
                if type(self.players[player_name]) == Hero:
                    self.map_array[pyrva][vtora - 1] = 'H'
                    self.map_array[pyrva][vtora] = '.'
                    self.players[player_name].j_coord -= 1
                elif type(self.players[player_name]) == Orc:
                    self.map_array[pyrva][vtora - 1] = 'O'
                    self.map_array[pyrva][vtora] = '.'
                    self.players[player_name].j_coord -= 1
            else:
                return False

        elif direction == "down":
            """if type(self.players[player_name]) == Hero and self.map_array[pyrva + 1][vtora] == 'O':
                fight = Fight(players[player_name], that_enemy(pyrva + 1, vtora))
            
            elif type(self.players[player_name]) == Orc and self.map_array[pyrva + 1][vtora] == 'H':
                fight = Fight(players[player_name], that_enemy(pyrva + 1, vtora)) """

            if self.map_array[pyrva + 1][vtora] == '.':
                if type(self.players[player_name]) == Hero:
                    self.map_array[pyrva + 1][vtora] = 'H'
                    self.map_array[pyrva][vtora] = '.'
                    self.players[player_name].i_coord += 1
                elif type(self.players[player_name]) == Orc:
                    self.map_array[pyrva + 1][vtora] = 'O'
                    self.map_array[pyrva][vtora] = '.'
                    self.players[player_name].i_coord += 1
            else:
                return False

        elif direction == "up":
            if type(self.players[player_name]) == Hero and self.map_array[pyrva - 1][vtora] == 'O':
                fight = Fight(players[player_name], that_enemy(pyrva - 1, vtora))
            
            elif type(self.players[player_name]) == Orc and self.map_array[pyrva - 1][vtora] == 'H':
                fight = Fight(players[player_name], that_enemy(pyrva - 1, vtora))

            if self.map_array[pyrva - 1][vtora] == '.':
                if type(self.players[player_name]) == Hero:
                    self.map_array[pyrva - 1][vtora] = 'H'
                    self.map_array[pyrva][vtora] = '.'
                    self.players[player_name].i_coord -= 1
                elif type(self.players[player_name]) == Orc:
                    self.map_array[pyrva - 1][vtora] = 'O'
                    self.map_array[pyrva][vtora] = '.'
                    self.players[player_name].i_coord -= 1
            else:
                return False




def main():
    map = Dungeon("dungeon_map")
    goshko = Hero("Hero", 100, "Hero")
    Orko = Orc("Orko", 100, 1.5)
    map.spawn("Goshko", goshko)
    map.move("Goshko", "right")
    map.print_map()
    print (map.players["Goshko"].i_coord, map.players["Goshko"].j_coord)
    print(map.move("Goshko", "down"))
    map.print_map()
    print (map.players["Goshko"].i_coord, map.players["Goshko"].j_coord)
    print(map.move("Goshko", "up"))
    map.print_map()
    print (map.players["Goshko"].i_coord, map.players["Goshko"].j_coord)

if __name__ == '__main__':
    main()
