from .player import Player
from ConnectNGame.src.players.random_ai import RandomAI
from typing import List
from ConnectNGame.src import move
from ConnectNGame.src.board import Board
from ConnectNGame.src import game
from main import ran_seed
import random
#inherits get_piece from RandomAi

class SimpleAI(RandomAI):

    def __init__(self,name: object, piece: object,game: "game.Game"):
        super().__init__(name,piece)
        self.game_playing = game


    def get_simple_name(players: List["Player"],num_player: int) -> str:
        name = "SimpleAI " + str(num_player)
        return name

    def create_Simple(players: List["Player"], blank_char: str,num_player: int, game: "game.Game")-> "SimpleAI":
        name = SimpleAI.get_simple_name(players,num_player)
        piece = SimpleAI.get_valid_piece(players, blank_char)
        return SimpleAI(name, piece,game)

    def get_move(self,board: Board) -> move.Move:
        if self.game_playing.players[0] == self:
            opp = self.game_playing.players[1]
        else:
            opp = self.game_playing.players[0]
        for cols in range(board.num_cols):
            if not board.is_column_full(cols):
                potential_move = move.Move(self, cols)
                potential_move.make(board)
                if potential_move.ends_game(self.game_playing):
                    board.remove_piece_from_column(cols)
                    return move.Move(self, cols)
                else:
                    board.remove_piece_from_column(cols)
        for coln in range(board.num_cols):
            if not board.is_column_full(coln):
                opp_move = move.Move(opp, coln)
                opp_move.make(board)
                if opp_move.ends_game(self.game_playing):
                    board.remove_piece_from_column(coln)
                    return move.Move(self, coln)
                else:
                    board.remove_piece_from_column(coln)
        possible_col = []
        for col in range(board.num_cols):
            if board.is_column_full(col) == False:
                possible_col.append(col)
        random.seed(ran_seed)
        choice = random.choice(possible_col)
        return move.Move(self, choice)


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

