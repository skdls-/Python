from random import randint
from player import Player
from bonus_functions import *


class Barbut():

    def __init__(self, players_count, points_to_win):
        self.players_count = players_count
        self.players = []
        for i in range(0, players_count):
            name = input("Name of next player: ")
            player = Player(name)
            self.players.append(player)
        self.current_player = 0
        self.points_to_win = points_to_win

    def print_scores(self):
        print ("----------------")
        for i in range(0, self.players_count):
            print (self.players[i].name)
            print (self.players[i].score)
        print ("----------------")

    def throw_dice(self, count):
        dices = []
        for i in range(0, count):
            dice = randint(1, 6)
            dices.append(dice)
        return dices

    def current_player(self):
        return self.players[current_player]

    def dice_combinations(self, dices):
        if dices == [1, 1, 1]:
            return 1000
        elif all_same_three(dices):
            return dices[0] * 100
        elif one_three_five(dices) or two_four_six(dices):
            return 200
        elif consecutive(dices):
            return 200
        elif 1 in dices or 5 in dices:
            ones_count = 0
            fives_count =0
            for dice in dices:
                if dice == 5:
                    fives_count += 1
                elif dice == 1:
                    ones_count += 1
            return ones_count * 100 + fives_count * 50
        else:
            return 0

    def game_finished(self):
        for player in self.players:
            if player.score > self.points_to_win:
                return True
        return False

    def iter_players(self):
        self.current_player += 1
        if self.current_player == self.players_count:
            self.current_player = 0
            self.print_scores()
        self.players[self.current_player].dices_to_risk_with = 3

    def player_turn(self, player):
        while self.players[self.current_player].dices_to_risk_with != 0:
            print (self.players[self.current_player].name, "'s turn: ")
            print ("Temp score:", self.players[self.current_player].temp_score)
            risk_it = input("Do you want to risk: y/n?")
            if risk_it == "n":
                self.players[self.current_player].score += self.players[self.current_player].temp_score
                self.players[self.current_player].temp_score = 0
                self.players[self.current_player].dices_to_risk_with = 3
                self.iter_players()
            elif risk_it == 'y':
                move = self.throw_dice(self.players[self.current_player].dices_to_risk_with)
                print (move)
                self.players[self.current_player].temp_score += self.dice_combinations(move)
                self.dices_to_risk_with(move, self.players[self.current_player])
                print("Dices  to risk with: ", self.players[self.current_player].dices_to_risk_with)
                self.player_turn(player)
        else:
            self.iter_players()
            return

    def dices_to_risk_with(self, dices, player):
        if dices == [1, 1, 1]:
            player.dices_to_risk_with = 3
        elif all_same_three(dices):
            player.dices_to_risk_with = 3
        elif one_three_five(dices) or two_four_six(dices):
            player.dices_to_risk_with = 3
        elif consecutive(dices):
            player.dices_to_risk_with = 3
        elif 1 in dices or 5 in dices:
            ones_fives_count = count_ones_and_fives(dices)
            if len(dices) == ones_fives_count:
                player.dices_to_risk_with = 3
            else:
                player.dices_to_risk_with = len(dices) - ones_fives_count
        else:
            player.dices_to_risk_with = 0

    def game(self):
        while not self.game_finished():
            current_player = self.current_player
            self.player_turn(self.players[current_player])
        else:
            print("Game Finished!")


barbut = Barbut(2, 5000)
barbut.game()
