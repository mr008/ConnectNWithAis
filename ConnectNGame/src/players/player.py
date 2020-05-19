from typing import List, Any
from ConnectNGame.src import move
from ConnectNGame.src.board import Board, BoardError
from abc import ABC, abstractmethod



class Player(ABC):
    def __init__(self, name: str, piece: str) -> None:
        self.name = name
        self.piece = piece

    def take_turn(self, the_board: Board) -> "move.Move":
        """
        Have the player take their turn
        :param the_board: the board to make their move on
        :return: the move the player made
        """
        while True:
            try:
                player_move = self.get_move(the_board)
                player_move.make(the_board)
            except (move.MoveError, BoardError) as error:
                print(error)
            else:
                return player_move

    @abstractmethod
    def get_valid_piece(players: List["Player"], blank_char: str, case_matters: bool = False) -> str:
        pass

    @abstractmethod
    def get_move(self, board: "Board") -> "move.Move":
        pass

    def __str__(self) -> str:
        return str(self.name)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Player) and \
               self.name == other.name and \
               self.piece == other.piece

    def __ne__(self, other: Any) -> bool:
        return not self == other

