import random
from .player import Player
from ConnectNGame.src.board import Board
from ConnectNGame.src import move

class RandomAi(Player):
    VISIBLE_CHARACTERS = [chr(i) for i in range(ord('!'), ord('~') + 1)]

    def __init__(self,):
        super.__init__(name,piece)
        #think about what else we need here

    def get_move(self,board) -> "move.Move":
        possible_col=[]
        for col in range(board.num_cols):
            if board.is_column_full(col) == False:
                possible_col.append(col)
        choice=random.choice(possible_col)
        return move.Move(self,choice)
    def get_name(self):
        ...
    def get_piece(self):
        ...
