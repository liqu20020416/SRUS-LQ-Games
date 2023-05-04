
from player import Player


class PlayerBNode:
    def __init__(self, player: Player):
        self.player = player
        self.left_tree = None
        self.right_tree = None

    @property
    def player(self):
        return self.player

    @property
    def left_tree(self):
        return self.left_tree

    @left_tree.setter
    def left_tree(self, value):
        self.left_tree = value

    @property
    def right_tree(self):
        return self.right_tree

    @right_tree.setter
    def set_right_tree(self, value):
        self.right_tree = value


