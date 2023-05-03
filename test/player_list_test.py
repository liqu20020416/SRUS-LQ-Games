import unittest
from player_list import PlayerList
from player import Player
from player_node import PlayerNode


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.list_case = PlayerList()
        self.player_case = Player("00000", "Li")
        self.player_case1 = Player("00001", "Li1")
        self.player_case2 = Player("00002", "Li2")

    def test_is_empty(self):
        self.assertEqual(self.list_case.is_it_empty(), True)

    def test_is_not_empty(self):
        self.list_case.add_at_head(self.player_case)
        self.assertEqual(self.list_case.is_it_empty(), False)

    def test_add_at_head(self):
        self.list_case.add_at_head(self.player_case)
        self.assertIsInstance(self.list_case._headList, PlayerNode)

    def test_add_at_tail(self):
        self.list_case.add_at_tail(self.player_case)
        self.assertIsInstance(self.list_case._tailList, PlayerNode)

    def test_delete_at_head(self):
        self.list_case.add_at_head(self.player_case)
        self.list_case.add_at_head(self.player_case1)
        self.list_case.delete_at_head()
        self.assertEqual(self.list_case._headList.key, self.player_case.uid)

    def test_delete_at_tail(self):
        self.list_case.add_at_tail(self.player_case)
        self.list_case.add_at_tail(self.player_case1)
        self.list_case.delete_at_tail()
        self.assertEqual(self.list_case._tailList.key, self.player_case.uid)
    def test_delete_node_based_key(self):
        self.list_case.add_at_head(self.player_case)
        self.list_case.add_at_head(self.player_case1)
        self.list_case.add_at_head(self.player_case2)
        self.list_case.delete_node_based_key("00000")
        self.assertEqual(self.list_case._headList.nextNode.key, "00001")
