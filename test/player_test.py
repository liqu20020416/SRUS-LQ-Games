import unittest

from app.player import Player


class TestCase(unittest.TestCase):
    def setUp(self):
        self.test_case = Player("00000", "Li")
        self.test_case.score = 125
        self.test_case1 = Player("00001", "Li1")
        self.test_case1.score = 130
        self.test_case2 = Player("00002", "Li2")
        self.test_case2.score = 150
        self.test_score_list = [self.test_case, self.test_case1, self.test_case2]
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

    def test_eq(self):
        self.assertFalse(self.test_case == self.test_case1)

    def test_lt(self):
        self.assertTrue(self.test_case < self.test_case2)

    def test_gt(self):
        self.assertTrue(self.test_case2 > self.test_case)

    def test_sort_score(self):
        Player.sort_score(self.test_score_list)
        self.assertEqual(self.test_score_list, [self.test_case2, self.test_case1, self.test_case])

