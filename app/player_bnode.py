from player import Player

class PlayerBNode:
    def __init__(self, player: Player):
        self._player = player
        self._left_tree = None
        self._right_tree = None

    @property
    def player(self):
        return self._player

    @property
    def left_tree(self):
        return self._left_tree

    @left_tree.setter
    def left_tree(self, value):
        self._left_tree = value

    @property
    def right_tree(self):
        return self._right_tree

    @right_tree.setter
    def right_tree(self, value):
        self._right_tree = value

    def sort_bst(self, name_key):
        if not name_key:
            return None
        mid_player = len(name_key)//2
        node = PlayerBNode(name_key[mid_player])
        node.left = self.sort_bst(name_key[:mid_player])
        node.right = self.sort_bst(name_key[mid_player+1:])
        return node

