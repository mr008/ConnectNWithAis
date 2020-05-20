from typing import List
from ConnectNGame.src.players.random_ai import RandomAI
from ConnectNGame.src import move
from ConnectNGame.src.board import Board
from ConnectNGame.src import game
from .player import Player
#inherits get_piece from RandomAi

class SimpleAI(RandomAI):

    def __init__(self, name: str, piece: str, game: "game.Game") -> None:
        super().__init__(name, piece)
        self.game_playing = game

    @staticmethod
    def get_simple_name(num_player: int) -> str:
        name = "SimpleAi " + str(num_player)
        return name

    @staticmethod
    def simple(players: List["Player"], blank_char: str, num_player: int, game: "game.Game") -> "SimpleAI":
        name = SimpleAI.get_simple_name(num_player)
        piece = SimpleAI.get_valid_piece(players, blank_char)
        return SimpleAI(name, piece, game)

    def get_move(self, board: Board) -> "move.Move":
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
        return super().get_move(board)