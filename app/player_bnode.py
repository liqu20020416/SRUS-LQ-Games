
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


