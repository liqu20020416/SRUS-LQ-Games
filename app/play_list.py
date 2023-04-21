from player_node import PlayerNode
from player import Player


class PlayerList:
    def __init__(self):
        self.headList: PlayerNode = None
        self.tailList: PlayerNode = None
        self.is_empty = True

    def add_at_head(self, player: Player):

        new_node = PlayerNode(player)

        if self.is_empty:
            self.headList = new_node
            self.tailList = new_node
            self.is_empty = False
        else:
            self.headList.previousNode = new_node
            new_node.nextNode = self.headList
            self.headList = new_node

    def add_at_tail(self, player: Player):
        new_node = PlayerNode(player)

        if self.is_empty:
            self.headList = new_node
            self.tailList = new_node
            self.is_empty = False
        else:
            self.tailListist.nextNode = new_node
            new_node.previousNode = self.tailList
            self.tailList = new_node

    @property
    def is_empty(self):
        return self.is_empty

