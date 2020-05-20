import unittest
import copy
from unittest.mock import patch
from ConnectNGame.src import player, board, move
from .print_capturer import PrintCapturer


class TestPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.other_players = [player.Player('Bob', 'X'), player.Player('Sally', 'O')]
        self.board = board.Board(4, 5, '#')

    def test_get_valid_piece(self):
        blank_char = self.board.blank_char
        inputs_and_answers = [
            ([''], 'Your piece cannot be the empty string or whitespace.'),
            (['   \t \t \t     \n'], 'Your piece cannot be the empty string or whitespace.'),
            (['X is a great choice'],
             f'X is a great choice is not a single character. Your piece can only be a single character.'),
            ([blank_char], 'Your piece cannot be the same as the blank character.'),
            (['x'], 'You cannot use x for your piece as Bob is already using it.'),
            (['o'], 'You cannot use o for your piece as Sally is already using it.')
        ]

        for user_input, error_msg in inputs_and_answers:
            with self.subTest(user_input=user_input):
                with patch('ConnectNGame.src.player.input', side_effect=user_input):
                    self.assertRaisesRegex(ValueError, error_msg,
                                           player.Player.get_valid_piece, self.other_players, blank_char)
        user_input = ['L']
        with self.subTest(user_input=user_input):
            with patch('ConnectNGame.src.player.input', side_effect=user_input):
                piece = player.Player.get_valid_piece(self.other_players, blank_char)
                self.assertEqual(user_input[0], piece)

    def test_get_valid_name(self):
        inputs_and_answers = [
            ([''], 'Your name cannot be the empty string or whitespace.'),
            (['   \t \t \t     \n'], 'Your name cannot be the empty string or whitespace.'),
            (['boB'], 'You cannot use boB for your name as someone else is already using it.'),
            (['SaLlY'], 'You cannot use SaLlY for your name as someone else is already using it.')
        ]

        for user_input, error_msg in inputs_and_answers:
            with self.subTest(user_input=user_input):
                with patch('ConnectNGame.src.player.input', side_effect=user_input):
                    self.assertRaisesRegex(ValueError, error_msg,
                                           player.Player.get_valid_name, self.other_players)

        user_input = ['bobert', 'sal', 'bo', 'joe']
        with patch('ConnectNGame.src.player.input', side_effect=user_input):
            for name in user_input:
                with self.subTest(name=name):
                    received_name = player.Player.get_valid_name(self.other_players)
                    self.assertEqual(name, received_name)

    def test_create_from_user_input(self):
        user_input = ['', '  ', 'Bob', 'Joe', '', 'Joe', ' ', 'Mike', 'o', 'Mike', self.board.blank_char, 'Wally', 'W']
        capture = PrintCapturer()
        print_output = ['Your name cannot be the empty string or whitespace.\n',
                        'Your name cannot be the empty string or whitespace.\n',
                        'You cannot use Bob for your name as someone else is already using it.\n',
                        'Your piece cannot be the empty string or whitespace.\n',
                        'Your piece cannot be the empty string or whitespace.\n',
                        'You cannot use o for your piece as Sally is already using it.\n',
                        'Your piece cannot be the same as the blank character.\n']
        answer_player = player.Player(*user_input[-2:])
        with patch('ConnectNGame.src.player.input', side_effect=user_input):
            with patch('ConnectNGame.src.player.print', side_effect=capture):
                new_player = player.Player.create_from_user_input(self.other_players, self.board.blank_char)
                self.assertEqual(answer_player, new_player)
                self.assertEqual(print_output, capture.output)

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

    def test_get_move(self):
        user_input = ['2']
        test_player = player.Player('George', 'P')
        answer = move.Move(test_player, 2)
        with patch('ConnectNGame.src.player.input', side_effect=user_input):
            user_move = test_player.get_move()
            self.assertEqual(answer, user_move)


if __name__ == '__main__':
    unittest.main()
