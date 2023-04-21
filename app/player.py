from argon2 import PasswordHasher
class Player:
    def __init__(self, uid: str, name: str):
        self._uid = uid
        self._name = name
        self.hashed_password = None
        self.argon2Hasher = PasswordHasher()

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

