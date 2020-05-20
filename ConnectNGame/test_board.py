import unittest
import copy

from ConnectNGame.src.board import Board, ColumnFullError, ColumnOutOfBoundsError


class TestBoard(unittest.TestCase):

    def test_num_rows(self):
        the_board = Board(3, 5, '*')
        self.assertEqual(3, the_board.num_rows)

    def test_num_cols(self):
        the_board = Board(3, 5, '*')
        self.assertEqual(5, the_board.num_cols)

    def test_is_full(self):
        the_board = Board(3, 5, '*')
        self.assertFalse(the_board.is_full)
        the_board.contents = [['X'] * 5] * 3
        self.assertTrue(the_board.is_full)
        the_board.contents[1][1] = '*'
        self.assertFalse(the_board.is_full)

    def test_is_column_in_bounds(self):
        the_board = Board(3, 5, '*')
        for i in range(-10, 10):
            with self.subTest(col=i):
                self.assertEqual(0 <= i < 5, the_board.is_column_in_bounds(i))

    def test_contains_blank_char(self):
        the_board = Board(3, 2, '*')
        the_board.contents = [['*', 'X'],
                              ['O', '*'],
                              ['*', 'J']]
        with self.subTest(msg='Should Contain Blanks'):
            self.assertTrue(the_board.contains_blank_character(0, 0))
            self.assertTrue(the_board.contains_blank_character(1, 1))
            self.assertTrue(the_board.contains_blank_character(2, 0))

        with self.subTest(msg='Should NOT Contain Blanks'):
            self.assertFalse(the_board.contains_blank_character(0, 1))
            self.assertFalse(the_board.contains_blank_character(1, 0))
            self.assertFalse(the_board.contains_blank_character(2, 1))

    def test_add_piece_to_column(self):
        the_board = Board(5, 6, '*')
        answer_contents = copy.deepcopy(the_board.contents)
        answer_heights = copy.deepcopy(the_board._number_of_pieces_in_columns)
        pieces_added = 0
        piece_to_add = 'X'
        # legal moves
        for row in range(the_board.num_rows):
            for col in range(the_board.num_cols):
                with self.subTest(row=row, col=col, pieces_added=pieces_added):
                    the_board.add_piece_to_column(piece_to_add, col)
                    answer_contents[row][col] = piece_to_add
                    answer_heights[col] += 1
                    self.assertEqual(answer_contents, the_board.contents)
                    self.assertEqual(answer_heights, the_board._number_of_pieces_in_columns)
                    pieces_added += 1

        # attempt to play in full column
        for col in range(the_board.num_cols):
            with self.subTest(col=col, msg='Play in full column'):
                self.assertRaises(ColumnFullError, the_board.add_piece_to_column, 'X', col)

        # attempt to play out of bounds
        for col in [-5, -3, -1, 10, 50, 6]:
            with self.subTest(col=col, msg='Play out of bounds'):
                self.assertRaises(ColumnOutOfBoundsError, the_board.add_piece_to_column, 'X', col)

    def test_remove_piece_from_column(self):
        the_board = Board(5, 6, '*')
        answer_contents = copy.deepcopy(the_board.contents)
        answer_heights = copy.deepcopy(the_board._number_of_pieces_in_columns)
        pieces_added = 0
        piece_to_add = 'X'

        # legal moves
        for row in range(the_board.num_rows):
            for col in range(the_board.num_cols):
                with self.subTest(row=row, col=col, pieces_added=pieces_added):
                    the_board.add_piece_to_column(piece_to_add, col)
                    answer_contents[row][col] = piece_to_add
                    answer_heights[col] += 1
                    self.assertEqual(answer_contents, the_board.contents)
                    self.assertEqual(answer_heights, the_board._number_of_pieces_in_columns)
                    pieces_added += 1
        the_board.remove_piece_from_column(3)
        answer_contents[4][3] = the_board.blank_char
        answer_heights[3] -= 1
        the_board.remove_piece_from_column(2)
        answer_contents[4][2] = the_board.blank_char
        answer_heights[2] -= 1
        the_board.remove_piece_from_column(0)
        answer_contents[4][0] = the_board.blank_char
        answer_heights[0] -= 1
        self.assertEqual(answer_contents, the_board.contents)
        self.assertEqual(answer_heights, the_board._number_of_pieces_in_columns)

    def test_count_max_matches(self):
        the_board = Board(4, 4, '*')
        the_board.contents = [['X', 'X', 'X', 'X'],
                              ['O', 'O', 'X', 'X'],
                              ['O', 'O', '*', 'X'],
                              ['O', '*', '*', 'O']]
        answers = [[4, 4, 4, 4],
                   [3, 2, 3, 3],
                   [3, 2, None, 3],
                   [3, None, None, 1]]

        for row_index, row in enumerate(answers):
            for col_index, count in enumerate(row):
                if count is not None:
                    with self.subTest(row=row_index, col=col_index):
                        self.assertEqual(count, the_board.count_max_matches(row_index, col_index))

    def test_count_matches_horizontally(self):
        the_board = Board(4, 4, '*')
        the_board.contents = [['X', 'X', 'X', 'X'],
                              ['O', 'O', 'X', 'X'],
                              ['O', 'O', '*', 'X'],
                              ['O', '*', '*', 'O']]
        answers = [[4, 4, 4, 4],
                   [2, 2, 2, 2],
                   [2, 2, None, 1],
                   [1, None, None, 1]]

        for row_index, row in enumerate(answers):
            for col_index, count in enumerate(row):
                if count is not None:
                    with self.subTest(row=row_index, col=col_index):
                        self.assertEqual(count, the_board.count_matches_horizontally(row_index, col_index))

    def test_count_matches_vertically(self):
        the_board = Board(4, 4, '*')
        the_board.contents = [['X', 'X', 'X', 'X'],
                              ['O', 'O', 'X', 'X'],
                              ['O', 'O', '*', 'X'],
                              ['O', '*', '*', 'O']]
        answers = [[1, 1, 2, 3],
                   [3, 2, 2, 3],
                   [3, 2, None, 3],
                   [3, None, None, 1]]

        for row_index, row in enumerate(answers):
            for col_index, count in enumerate(row):
                if count is not None:
                    with self.subTest(row=row_index, col=col_index):
                        self.assertEqual(count, the_board.count_matches_vertically(row_index, col_index))

    def test_count_matches_in_right_diagonal_win(self):
        """
        Count the number of uninterrupted matches to the piece at row,col in this direction
            X
          X
        X
        """
        the_board = Board(4, 4, '*')
        the_board.contents = [['X', 'X', 'X', 'X'],
                              ['O', 'O', 'X', 'X'],
                              ['O', 'O', '*', 'X'],
                              ['O', '*', '*', 'O']]
        answers = [[1, 1, 1, 2],
                   [1, 2, 2, 1],
                   [2, 2, None, 1],
                   [2, None, None, 1]]

        for row_index, row in enumerate(answers):
            for col_index, count in enumerate(row):
                if count is not None:
                    with self.subTest(row=row_index, col=col_index):
                        self.assertEqual(count, the_board.count_matches_in_right_diagonal(row_index, col_index))

    def test_count_matches_in_left_diagonal(self):
        """
        Count the number of uninterrupted matches to the piece at row,col in this direction
        X
          X
            X
        """
        the_board = Board(4, 4, '*')
        the_board.contents = [['X', 'X', 'X', 'X'],
                              ['O', 'O', 'X', 'X'],
                              ['O', 'O', '*', 'X'],
                              ['O', '*', '*', 'O']]
        answers = [[1, 3, 2, 1],
                   [2, 1, 3, 2],
                   [1, 2, None, 3],
                   [1, None, None, 1]]

        for row_index, row in enumerate(answers):
            for col_index, count in enumerate(row):
                if count is not None:
                    with self.subTest(row=row_index, col=col_index):
                        self.assertEqual(count, the_board.count_matches_in_left_diagonal(row_index, col_index))

    def test_iter(self):
        the_board = Board(4, 4, '*')
        the_board.contents = [['X', 'X', 'X', 'X'],
                              ['O', 'O', 'X', 'X'],
                              ['O', 'O', '*', 'X'],
                              ['O', '*', '*', 'O']]
        for answer, value in zip(the_board, the_board.contents):
            self.assertEqual(answer, value)

    def test_column_iterate(self):
        the_board = Board(4, 4, '*')
        the_board.contents = [['X', 'X', 'X', 'X'],
                              ['O', 'O', 'X', 'X'],
                              ['O', 'O', '*', 'X'],
                              ['O', '*', '*', 'O']]
        columns = [['X', 'O', 'O', 'O'],
                   ['X', 'O', 'O', '*'],
                   ['X', 'X', '*', '*'],
                   ['X', 'X', 'X', 'O']]

        for answer, value in zip(columns, the_board.column_iterate()):
            self.assertSequenceEqual(answer, value)


if __name__ == '__main__':
    unittest.main()

