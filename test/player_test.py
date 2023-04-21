import unittest

from app.player import Player

class testCase(unittest.TestCase):
    def setUp(self):
       self.test_case = Player("00000", "Li")


    def test_uid(self):
        self.assertEqual(self.test_case.uid, "00000")

    def test_name(self):
        self.assertEqual(self.test_case.name,"Li")