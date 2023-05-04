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
            name_key = self._root
            if name_key is None:
                self._root = player
                return

        if str(name_key) > str(player):
            if name_key.right_tree is None:
                name_key.right_tree = player
                return
            self.insert_player(player, name_key.right_tree)

        elif str(name_key) < str(player):
            if name_key.left_tree is None:
                name_key.left_tree = player
                return
            self.insert_player(player, name_key.left_tree)

        else:
            self.insert_player(player)
            player.name = str(input("Duplicated Name! Please enter player name:"))

    def search(self, name: str, name_key=None):
        if name_key is None:
            name_key = self._root
            if name_key is None:
                return print("This BST is empty!")

        if str(name_key.player.name) > str(name):
            if name_key.right_tree is None:
                return print("The name is not exist!")
            self.insert_player(name, name_key.right_tree)

        elif str(name_key.player.name) < str(name):
            if name_key.left_tree is None:
                return print("The name is not exist!")
            self.insert_player(name, name_key.left_tree)

        else:
            self.insert_player(name_key.player.name)
            name_key.player.name = str(input("Duplicated Name! Please enter player name:"))