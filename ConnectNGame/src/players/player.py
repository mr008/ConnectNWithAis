from typing import List, Any
from . import move
from .board import Board, BoardError


class Player(object):

    @staticmethod
    def create_from_user_input(players: List["Player"], blank_char: str) -> "Player":
        """
        Create player for user input
        :param players: The other players in the game
        :param blank_char: The blank character in the board
        :return: A player created from this user's input
        """
        while True:
            try:
                name = Player.get_valid_name(players)
                piece = Player.get_valid_piece(players, blank_char)
                return Player(name, piece)
            except ValueError as error:
                print(error)

    @staticmethod
    def get_valid_piece(players: List["Player"], blank_char: str, case_matters: bool = False) -> str:
        """
        Check if piece is a valid one to use in the current game.
        A piece is valid if it is 1 character big
        and no other players are using it.
        :param players: The other players in the game
        :param blank_char: The blank character for the board
        :param case_matters: Does case matter when comparing pieces?
        :return: the piece the player has chosen
        :raises ValueError if the piece is not valid
        """
        player_num = len(players) + 1
        piece = input(f'Player {player_num} enter your piece: ').strip()
        cmp_piece = piece if case_matters else piece.lower()
        player_pieces = {player.piece if case_matters else player.piece.lower(): player for player in players}

        if not piece:
            raise ValueError('Your piece cannot be the empty string or whitespace.')
        elif len(piece) > 1:
            raise ValueError(f'{piece} is not a single character. Your piece can only be a single character.')
        elif cmp_piece == blank_char.lower():
            raise ValueError(f'Your piece cannot be the same as the blank character.')
        elif cmp_piece in player_pieces:
            raise ValueError(
                f'You cannot use {piece} for your piece as {player_pieces[cmp_piece]} is already using it.')
        else:
            return piece

    @staticmethod
    def get_valid_name(players: List["Player"], case_matters: bool = False) -> str:
        """
        Check if name is a valid name for this player
        :param players:  The other players in the game
        :param case_matters: Whether capitalization matters or not
        :return: The name the user has chosen
        :raises: ValueError if the name chosen is not vlaid

        """
        player_num = len(players) + 1
        player_names = {player.name if case_matters else player.name.lower() for player in players}
        name = input(f'Player {player_num} enter your name: ').strip()
        cmp_name = name if case_matters else name.lower()
        if not name:
            raise ValueError('Your name cannot be the empty string or whitespace.')
        elif cmp_name in player_names:
            raise ValueError(f'You cannot use {name} for your name as someone else is already using it.')
        else:
            return name

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
                player_move = self.get_move()
                player_move.make(the_board)
            except (move.MoveError, BoardError) as error:
                print(error)
            else:
                return player_move

    def get_move(self) -> "move.Move":
        """
        Get a move from the user
        :return: the move the user made
        :raises: MoveError if the move is invalid
        """
        str_move = input(f'{self.name}, please enter the column you want to play in: ')
        return move.Move.from_string(self, str_move)

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Player) and \
               self.name == other.name and \
               self.piece == other.piece

    def __ne__(self, other: Any) -> bool:
        return not self == other

