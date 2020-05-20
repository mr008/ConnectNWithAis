import unittest
from ConnectNGame.src.players.simple_ai import SimpleAI
from ConnectNGame.src.board import Board
from ConnectNGame.src.game import Game

class TestSimpleAi(unittest.TestCase):
    def test_get_simple_name(self):
        board1=Board(3,3,"*")
        mygame=Game(board1,3)
        ai = SimpleAI("Boss","%",mygame)
        ai.get_name(3)
        self.assertEqual(ai.get_name(3), "RandomAi 3")

if __name__ == '__main__':
    unittest.main()