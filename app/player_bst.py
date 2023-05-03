from player import Player


class PlayerBST:
    def __init__(self, root):
        self.root = None

    @property
    def root(self):
        return self.root

    def insert(self, player: Player, name_key=None):
        if name_key is None:
            name_key = self.root
            if name_key is None:
               self.root = self.player

        if name_key > player:
            if name_key.left_tree is None:
                name_key.left_tree = player
            self.insert(player, name_key.left_tree)

        elif name_key < player:
            if name_key.right_tree is None:
                name_key.right_tree = player
            self.insert(player, name_key.right_tree)

        else:
            self.insert(player)