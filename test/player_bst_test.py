import unittest
from app.player_bnode import PlayerBNode
from app.player_bst import PlayerBST
from app.player import Player


class TestPlayerBST(unittest.TestCase):

    def setUp(self):
        self.player_case = PlayerBNode(Player("00000", "Ai"))
        self.player_case1 = PlayerBNode(Player("00001", "Bi"))
        self.player_case2 = PlayerBNode(Player("00002", "Ci"))
        self.bst_list = PlayerBST()

    def test_insert_player(self):
        self.bst_list.insert(self.player_case)
        self.assertEqual(self.bst_list.root, self.player_case)

    def test_insert_player_right(self):
        self.bst_list.insert_player(self.player_case)
        self.bst_list.insert_player(self.player_case1)
        self.assertEqual(self.bst_list.root.right_tree, self.player_case1)

    def test_search(self):
        self.bst_list.search(self.player_case)
        self.assertEqual(self.bst_list.root, None)
