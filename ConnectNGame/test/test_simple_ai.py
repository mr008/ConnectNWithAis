import unittest
from ConnectNGame.src.players import simple_ai


class MyTestCase(unittest.TestCase):
    def test_get_simple_name(self):
        ai = simple_ai.SimpleAI("Boss","%",game)
        ai.get_name(3)
        self.assertEqual(ai.get_name(3), "RandomAi 3")


if __name__ == '__main__':
    unittest.main()
