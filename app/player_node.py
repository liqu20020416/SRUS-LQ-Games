from player import Player


class PlayerNode:
    def __init__(self, player: Player):
        self.player = player
        self.nextNode = None
        self.previousNode = None

    @property
    def theplayer(self):
        return self.player

    @theplayer.setter
    def theplayer(self, value):
        self.player = value

    @property
    def thenext(self):
        return self.nextNode

    @thenext.setter
    def thenext(self, value):
        self.nextNode = value

    @property
    def theprev(self):
        return self.previousNode

    @theprev.setter
    def theprev(self, value):
        self.previousNode = value
    @property
    def key(self):
        return self.player.uid

    def __str__(self):
        return f"Player Name is {self.player.name} \n Player ID is {self.player.uid} \n Next Node is {self.nextNode} \n Previous Node is {self.previousNode}"






