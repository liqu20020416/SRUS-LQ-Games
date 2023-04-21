from player import Player


class PlayerNode:
    def __init__(self, player):
        self.player = player
        self.nextNode = None
        self.previousNode = None

    @property
    def get_player(self):
        return self.player

    @get_player.setter
    def set_player(self, value):
        self.player = value

    @property
    def get_nextNode(self):
        return self.nextNode

    @get_nextNode.setter
    def set_nextNode(self, value):
        self.nextNode = value

    @property
    def get_previousNode(self):
        return self.previousNode

    @get_previousNode.setter
    def set_previousNode(self, value):
        self.previousNode = value

    @property
    def key(self):
        return self.player.uid

    def __str__(self):
        return f"Player is {self.player} \n Next Node is {self.nextNode}  \n Previous Node is {self.previousNode}"
