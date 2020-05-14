import sys
from ConnectNGame.src.game import Game


def main() -> None:
    """
    Run the program
    :return:
    """
    if len(sys.argv) == 2:
        connectn = Game.create_game_from_file(sys.argv[1])
        connectn.play()
    elif len(sys.argv) < 2:
        print('Not enough command line arguments')
        print('Usage: python3 main.py path_to_config_file')
    else:
        print('Too many command line arguments ')
        print('Usage: python3 main.py path_to_config_file')


if __name__ == '__main__':
    main()

