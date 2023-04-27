from argon2 import PasswordHasher
class Player:
    def __init__(self, uid: str, name: str):
        self._uid = uid
        self._name = name
        self.hashed_password = None
        self.argon2Hasher = PasswordHasher()
        self.score = 0

    def __str__(self):
        return f"Player name is : {self._name} \n Player ID is: {self._uid}"

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name

    def add_password(self, password: str):
        self.hashed_password = self.argon2Hasher.hash(password)

    def verify_password(self, password: str):
        if self.argon2Hasher.verify(self.hashed_password, password):
            return True
        else:
            return False

    @property
    def get_score(self):
        return self.score

    @get_score.setter
    def set_score(self, value):
        self.score = value

    def __eq__(self, compareWith):
        return self.score == compareWith.score

    def __lt__(self, compareWith):
        return self.score < compareWith.score

    def __gt__(self, compareWith):
        return self.score > compareWith.score

    @staticmethod
    def sort_score(players):
        for i in range(len(players)):
            min_score = i
            for j in range(i + 1, len(players)):
                if players[min_score] < players[j]:
                    min_score = j
            players[i], players[min_score] = players[min_score], players[i]


