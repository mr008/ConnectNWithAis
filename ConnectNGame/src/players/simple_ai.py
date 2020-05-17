from ConnectNGame.src.players.player import Player
from ConnectNGame.src.players.random_ai import RandomAI
from typing import List
#inherits get_piece from RandomAi

class SimpleAI(RandomAI):
    ...
    def __init__(self):
        super().__init__()

    def get_move(self) -> "move.Move":
        pass

    def get_simple_name(self,players: List["Player"]):
        name = "SimpleAI " + str(len(players) + 1)
        return name