import unittest

from app.player import Player


class TestCase(unittest.TestCase):
    def setUp(self):
        self.test_case = Player("00000", "Li")

    def test_uid(self):
        self.assertEqual(self.test_case.uid, "00000")

    def test_name(self):
        self.assertEqual(self.test_case.name, "Li")

    def test_add_password(self):
        self.test_case.add_password("20020416")
        self.assertNotEqual(self.test_case.hashed_password, None)

    def test_verify_password(self):
        self.test_case.add_password("20020416")
        self.assertTrue(self.test_case.argon2Hasher.verify(self.test_case.hashed_password, "20020416"))

