import unittest
from app.play_list import PlayerList
from app.player import Player
from app.player_node import PlayerNode


class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.list_case = PlayerList()
        self.player_case = Player("00000", "Li")

    def test_is_empty(self):
        self.assertEqual(self.list_case.is_empty(), True)

    def test_add_at_head_is_empty(self):
        self.list_case.add_at_head(self.player_case)
        self.assertEqual(self.list_case.is_empty(), False)



