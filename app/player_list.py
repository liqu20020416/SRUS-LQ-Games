from player_node import PlayerNode
from player import Player


class PlayerList:
    def __init__(self):
        self._headList: PlayerNode = None
        self._tailList: PlayerNode = None
        self._is_empty = True

    def add_at_head(self, player: Player):
        new_node = PlayerNode(player)
        if self._is_empty:
            self._is_empty = False
            self._headList = new_node
            self._tailList = new_node
        else:
            self._headList.previousNode = new_node
            new_node.nextNode = self._headList
            self._headList = new_node

    def add_at_tail(self, player: Player):
        new_node = PlayerNode(player)
        if self._is_empty:
            self._is_empty = False
            self._headList = new_node
            self._tailList = new_node
        else:
            self._tailList.nextNode = new_node
            new_node.previousNode = self._tailList
            self._tailList = new_node

    def delete_at_head(self):
        self._headList = self._headList.nextNode
        self._headList.previousNode = None

    def delete_at_tail(self):
        self._tailList = self._tailList.previousNode
        self._tailList.nextNode = None



    def is_it_empty(self):
        return self._is_empty
