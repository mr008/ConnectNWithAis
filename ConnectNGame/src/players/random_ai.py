
from .player import Player


class RandomAi(Player):
    VISIBLE_CHARACTERS = [chr(i) for i in range(ord('!'), ord('~') + 1)]
