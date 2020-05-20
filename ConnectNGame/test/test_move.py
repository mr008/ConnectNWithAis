import unittest
from ConnectNGame.src import move, game, player, board


class TestMove(unittest.TestCase):
    def test_from_string(self):
        test_player = player.Player('Bob', 'X')
        invalid_moves = ['hi', '1.2', '3 5']
        for bad_move in invalid_moves:
            with self.subTest(move=bad_move):
                self.assertRaises(move.MoveFormatError, move.Move.from_string, test_player, bad_move)

        valid_moves = ['2', '3', '1']
        for valid_move in valid_moves:
            with self.subTest(move=valid_move):
                answer = move.Move(test_player, int(valid_move))
                test_move = move.Move.from_string(test_player, valid_move)
                self.assertEqual(answer, test_move)

    def test_make(self):
        test_player = player.Player('Bob', 'X')
        test_move = move.Move(test_player, 2)
        test_board = board.Board(5, 4, 'M')
        test_move.make(test_board)
        answer_board = board.Board(5, 4, 'M')
        answer_board[2][0] = 'X'
        answer_board._number_of_pieces_in_columns = [0, 0, 1, 0]
        self.assertEqual(answer_board, test_board)

    def test_ends_game(self):
        the_board = board.Board(4, 4, '*')
        the_board.contents = [['X', 'X', 'X', 'X'],
                              ['O', 'O', 'X', 'X'],
                              ['O', 'O', '*', 'X'],
                              ['O', '*', '*', 'O']]
        the_board._number_of_pieces_in_columns = [4, 3, 2, 4]
        players = [player.Player('Bob', 'X'), player.Player('Sally', 'S')]
        test_game = game.Game(the_board, 4, players)
        test_move = move.Move(players[0], 2)
        test_move.make(the_board)
        self.assertFalse(test_move.ends_game(test_game))
        test_move.make(the_board)
        self.assertTrue(test_move.ends_game(test_game))


if __name__ == '__main__':
    unittest.main()