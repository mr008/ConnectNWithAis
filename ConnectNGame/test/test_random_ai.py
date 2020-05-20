import unittest
from unittest.mock import patch, mock_open
from ConnectNGame.src import game, board
from ConnectNGame.src.players import random_ai
from ConnectNGame.src.board import Board
from ConnectNGame.src import move
from ConnectNGame.src.players.random_ai import RandomAI
from ConnectNGame.src.players.human_player import HumanPlayer
import random

class MyTestCase(unittest.TestCase):

    def test_get_name(self):
        name = RandomAI.get_name(1)
        self.assertEqual(name, "RandomAi 1")

    def test_get_valid_piece(self):
        my_players = [HumanPlayer('sam', '#'),HumanPlayer('Jess', '@')]
        my_piece = RandomAI.get_valid_piece(my_players, '$')
        self.assertIsNot(my_piece, my_players[0].piece, my_players[1].piece)
        self.assertIsNot(my_piece,'$')
        self.assertIsNot(my_piece,' ')

if __name__ == '__main__':
    unittest.main()