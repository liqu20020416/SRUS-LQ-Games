class PlayerBNode:
    def __init__(self, player):
        self.player = player
        self.left_tree = None
        self.right_tree = None

    @property
    def player(self):
        return self.player

    @property
    def get_left_tree(self):
        return self.left_tree

    @get_left_tree.setter
    def set_left_tree(self, value):
        self.left_tree = value

    @property
    def get_right_tree(self):
        return self.right_tree

    @get_right_tree.setter
    def set_right_tree(self, value):
        self.right_tree = value

