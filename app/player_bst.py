from player import Player
from player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value

    def insert_player(self, player: PlayerBNode, name_key=None):
        if name_key is None:
            name_key = self.root
            if name_key is None:
                self.root = player
                return

        if name_key > player:
            if name_key.right_tree is None:
                name_key.right_tree = player
                return
            self.insert_player(player, name_key.right_tree)

        elif name_key < player:
            if name_key.left_tree is None:
                name_key.left_tree = player
                return
            self.insert_player(player, name_key.left_tree)

        else:
            self.insert_player(player, name_key.right_tree)
            player.name = str(input("Duplicated Name! Please enter player name:"))

