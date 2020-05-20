import sys
import random
from random import seed
from ConnectNGame.src.game import Game


def main() -> None:
    """
    Run the program
    :return:
    """
    address = "E:/coding programs/ConnectNWithAis/config_files/3X3X3.txt"
    #ran_seed=30
    #random.seed(ran_seed)
    #address = "/Users/audeclairemoats/PycharmProject/ConnectN/config_files/3X3X3.txt"
    '''
    if len(sys.argv) == 2:
        address = sys.argv[1]
        connectn = Game.create_game_from_file(address)
        connectn.play()
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        ran_seed = int(sys.argv[2])
        random.seed(ran_seed)
        connectn = Game.create_game_from_file(address)
        connectn.play()

    elif len(sys.argv) < 2:
        print('Not enough command line arguments')
        print('Usage: python3 main.py path_to_config_file')
    else:
        print('Too many command line arguments ')
        print('Usage: python3 main.py path_to_config_file')
    '''
    #connectn = Game.create_game_from_file(address)
    #connectn.play()

if __name__ == '__main__':
    main()