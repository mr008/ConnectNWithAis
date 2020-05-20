import unittest
from unittest.mock import patch, mock_open
from ConnectNGame.src import game, board
from ConnectNGame.src.players import random_ai
from ConnectNGame.src.board import Board
from ConnectNGame.src import move
from ConnectNGame.src.players.random_ai import RandomAI
import random

class MyTestCase(unittest.TestCase):

    def test_get_name(self):
        ai=RandomAI("ai","*")
        ai.get_name(1)
        self.assertEqual(ai.get_name(1),"RandomAi 1")
    def test_random(self):
        RandomAI.random([],"*",1)
        self.assertEqual()

    def
    self.assertEqual

if __name__ == '__main__':
    unittest.main()
