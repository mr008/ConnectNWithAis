import sys
from ConnectNGame.src.game import Game


def main() -> None:
    """
    Run the program
    :return:
    """
    address = "E:\coding programs\ConnectNWithAis\config_files\\3X3X3.txt"
    connectn = Game.create_game_from_file(address)
    connectn.play()
"""
    if len(sys.argv) == 2:
        #address=sys.argv[1]
        address="E:\coding programs\ConnectNWithAis\config_file\3X3X3.txt"
        connectn = Game.create_game_from_file(address)
        connectn.play()
    elif len(sys.argv) < 2:
        print('Not enough command line arguments')
        print('Usage: python3 main.py path_to_config_file')
    else:
        print('Too many command line arguments ')
        print('Usage: python3 main.py path_to_config_file')
"""

if __name__ == '__main__':
    main()

