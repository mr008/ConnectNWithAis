from .player import Player
from ConnectNGame.src.players.random_ai import RandomAI
from typing import List
from ConnectNGame.src import move
from ConnectNGame.src.board import Board
from ConnectNGame.src import game
import random
#inherits get_piece from RandomAi

class SimpleAI(RandomAI):

    def __init__(self,name: object, piece: object,game: "game.Game"):
        super().__init__(name,piece)
        self.game_playing = game


    def get_simple_name(players: List["Player"],num_player: int):
        name = "SimpleAI " + str(num_player)
        return name

    def create_Simple(players: List["Player"], blank_char: str,num_player: int, game: "game.Game"):
        name = SimpleAI.get_simple_name(players,num_player)
        piece = SimpleAI.get_valid_piece(players, blank_char)
        return SimpleAI(name, piece,game)

    def get_move(self,board) -> move.Move:
    '''ai_piece=self.piece
        if self.name[-1] == '2':
            opp_number=0
        elif self.name[-1] == '1':
            opp_number=1
        for col in range(board.num_cols):
            board.add_piece_to_column(ai_piece,col)
            number_pieces_column=board.get_column_pieces()
            if game.Game.is_part_of_win(number_pieces_column+1,col) == True:
                choice=col
                board.sub_piece_to_column(ai_piece, col)
                return move.Move(self,choice)
            board.sub_piece_to_column(ai_piece, col)
        opp_piece = game.players[opp_number].piece
        for col in range(board.num_cols):
            board.add_piece_to_column(opp_piece, col)
            number_pieces_column = board.get_column_pieces()
            if game.Game.is_part_of_win(number_pieces_column + 1, col) == True:
                choice = col
                board.sub_piece_to_column(opp_piece, col)
                return move.Move(self, choice)
            board.sub_piece_to_column(opp_piece, col)
            super().get_move(board)
    '''

