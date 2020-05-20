import unittest
import copy
from unittest.mock import patch
from ConnectNGame.src import player, board, move
from .print_capturer import PrintCapturer


class TestPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.other_players = [player.Player('Bob', 'X'), player.Player('Sally', 'O')]
        self.board = board.Board(4, 5, '#')

    def test_take_turn(self):
        test_player = player.Player('George', 'P')
        the_board = board.Board(4, 4, '*')
        the_board.contents = [['X', 'X', 'X', 'X'],
                              ['O', 'O', 'X', 'X'],
                              ['O', 'O', '*', 'X'],
                              ['O', '*', '*', 'O']]
        the_board._number_of_pieces_in_columns = [4, 3, 2, 4]

        answer_board = copy.deepcopy(the_board)
        answer_board.contents[3][1] = 'P'
        answer_board._number_of_pieces_in_columns[1] += 1

        user_input = ['hello', '-1', '4', '3', '1']
        capture = PrintCapturer()
        output = ['George, column needs to be an integer. hello is not an integer. \n',
                  'Your column needs to be between 0 and 3 but is actually -1.\n',
                  'Your column needs to be between 0 and 3 but is actually 4.\n',
                  'You cannot play in 3 because it is full.\n']
        with patch('ConnectNGame.src.player.input', side_effect=user_input):
            with patch('ConnectNGame.src.player.print', side_effect=capture):
                test_player.take_turn(the_board)
                self.assertEqual(answer_board, the_board)
                self.assertEqual(output, capture.output)

if __name__ == '__main__':
    unittest.main()
