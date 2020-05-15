from ConnectNGame.src.players.player import Player


class HumanPlayer(Player):
    def __init__(self,name: object, piece: object):
        super().__init__(name, piece)

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

