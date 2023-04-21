
class Player:
    def __init__(self, uid: str, name: str):
        self._uid = uid
        self._name = name


    def __str__(self):
        return f"Player name is : {self._name} \n Player ID is: {self._uid}"

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name