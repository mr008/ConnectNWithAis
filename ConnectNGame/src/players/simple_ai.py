from .player import Player
from ConnectNGame.src.players.random_ai import RandomAI
from typing import List
#inherits get_piece from RandomAi

class SimpleAI(RandomAI):
    ...
    def __init__(self):
        super().__init__()

    def get_move(self) -> "move.Move":
        pass

    def get_simple_name(players: List["Player"]):
        name = "SimpleAI " + str(len(players) + 1)
        return name

    def create_Simple(players: List["Player"], blank_char: str):
        name = SimpleAI.get_simple_name(players)
        piece = SimpleAI.get_valid_piece(players, blank_char)
        return SimpleAI(name, piece)