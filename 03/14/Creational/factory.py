from abc import ABC, abstractmethod
from random import choice


class PlayerBase(ABC):
    choices = ['r', 'p', 's']

    @abstractmethod
    def move(self):
        pass


class HumanPlayer(PlayerBase):
    def move(self):
        m = input("Choose your next move: ")


class SystemPlayer(PlayerBase):
    def move(self):
        return choice(self.choice)


class Game:  
    @staticmethod
    def start_game():
        game_type = input("Please choose game type (s 's' for single and 'm' for multiple player: ")
        
        if game_type == 's':
            p1 = HumanPlayer()
            p2 = SystemPlayer
        if game_type == 'm':
            p1 = HumanPlayer()
            p2 = HumanPlayer()
        else:
            print("invalid input")
            p1 = None
            p2 = None
        return p1, p2


if __name__ == "__main__":
    game= Game()
    player_1, player_2 = Game.start_game()

    for player in[player_1, player_2]:
        player.move()