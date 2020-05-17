from .player import Player
from ConnectNGame.src.players.random_ai import RandomAI
from ConnectNGame.src import move
from typing import List
#inherits get_piece from RandomAi

class SimpleAI(RandomAI):
    ...
    def __init__(self):
        super().__init__()

    def get_move(self) -> "move.Move":
        pass

    def get_simple_name(players: List["Player"],num_player: int):
        name = "SimpleAI " + str(num_player)
        return name

    def create_Simple(players: List["Player"], blank_char: str):
        name = SimpleAI.get_simple_name(players)
        piece = SimpleAI.get_valid_piece(players, blank_char)
        return SimpleAI(name, piece)

    def move(self,board,game):
        for col in range(board.num_cols):
            number_pieces_column=board.get_column_pieces()
            if game.is_part_of_win(number_pieces_column+1,col) == True:
                choice=col
                return move.Move(self,choice)
        for col in range(board.num_cols):
            number_pieces_column=board.get_column_pieces()
            if game.is_part_of_win(number_pieces_column+1,col) == True:
                choice=col
                return move.Move(self,choice)
        super().get_move()

