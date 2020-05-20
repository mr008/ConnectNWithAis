import unittest
from ConnectNGame.src.players.simple_ai import SimpleAI


class MyTestCase(unittest.TestCase):

    def test_get_simple_name(self):
        name = SimpleAI.get_name(2)
        self.assertEqual(name, "SimpleAi 2")


if __name__ == '__main__':
    unittest.main()
