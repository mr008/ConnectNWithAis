from .player import Player
from ConnectNGame.src.players.random_ai import RandomAI
from ConnectNGame.src import game
from ConnectNGame.src import move
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

    def get_move(self,board,game):
        ai_piece=1
        for col in range(board.num_cols):
            board.add_piece_to_column(ai_piece,col)
            number_pieces_column=board.get_column_pieces()
            if game.Game.is_part_of_win(number_pieces_column+1,col) == True:
                choice=col
                board.sub_piece_to_column(ai_piece, col)
                return move.Move(self,choice)
            board.sub_piece_to_column(ai_piece, col)
        opp_piece = self.piece
        for col in range(board.num_cols):
            board.add_piece_to_column(opp_piece, col)
            number_pieces_column = board.get_column_pieces()
            if game.Game.is_part_of_win(number_pieces_column + 1, col) == True:
                choice = col
                board.sub_piece_to_column(opp_piece, col)
                return move.Move(self, choice)
            board.sub_piece_to_column(opp_piece, col)
        super().get_move()

