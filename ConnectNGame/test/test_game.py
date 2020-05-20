import unittest
from unittest.mock import patch, mock_open
from ConnectNGame.src import game, board, player


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        answer_board = board.Board(6, 7, '*')
        answer_players = [player.Player('Bob', 'X'), player.Player('Joe', 'L')]

        self.game = game.Game(answer_board, 4, answer_players)

    def test_create_from_file(self):
        answer_board = board.Board(6, 7, '*')
        answer_players = [player.Player('Bob', 'X'), player.Player('Joe', 'L')]

        user_input = ['Bob', 'X', 'Joe', 'L']
        with patch('ConnectNGame.src.player.input', side_effect=user_input):
            with patch('ConnectNGame.src.game.open',
                       new=mock_open(read_data='num_rows : 6\nnum_cols : 7\nnum_pieces_to_win : 4\nblank_char : *')):
                g = game.Game.create_game_from_file('dummy')
                self.assertEqual(answer_board, g.board)
                self.assertEqual(answer_players, g.players)
                self.assertEqual(4, g.num_pieces_to_win)

    def test_change_turn(self):
        for turn in range(10):
            with self.subTest(turn=turn):
                if turn % 2 == 0:
                    self.assertIs(self.game.players[0], self.game.cur_player)
                else:
                    self.assertIs(self.game.players[1], self.game.cur_player)
                self.game.change_turn()

    def test_is_part_of_win(self):
        self.game.board.contents = [['L', 'X', 'X', 'X', 'X', 'X', 'L'],
                                    ['X', 'L', 'X', 'L', 'L', 'L', 'X'],
                                    ['X', 'L', 'L', 'L', 'L', 'L', 'X'],
                                    ['*', 'L', 'X', 'L', '*', 'L', 'X'],
                                    ['*', 'L', 'X', '*', '*', '*', 'L'],
                                    ['*', 'L', 'X', '*', '*', '*', 'X']]
        answers = [[True, True, True, True, True, True, True],
                   [False, True, False, True, False, True, False],
                   [False, True, True, True, True, True, False],
                   [None, True, False, True, None, True, False],
                   [None, True, False, None, None, None, True],
                   [None, True, False, None, None, None, False]]
        for row_index, row in enumerate(answers):

            for col_index, answer in enumerate(row):
                with self.subTest(row=row_index, col=col_index):
                    if answer is None:
                        self.assertRaises(ValueError, self.game.is_part_of_win, row_index, col_index)
                    else:
                        self.assertEqual(answer, self.game.is_part_of_win(row_index, col_index))

    def test_setup_players(self):



if __name__ == '__main__':
    unittest.main()
