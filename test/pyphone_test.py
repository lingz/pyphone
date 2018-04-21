import unittest
import pyphone


class PyphoneTest(unittest.TestCase):
    def test_phonex(self):
        self.assertEqual(pyphone.phonex('hello'),
                         [(19, 1, 18, 3)])
        self.assertEqual(sorted(pyphone.phonex('world')),
                         [(16, 3, 22, 18, 13), (16, 5, 18, 13)])
        self.assertEqual(sorted(pyphone.phonex('friend')),
                         [(12, 22, 2, 1, 17, 13), (12, 22, 7, 17, 13)])
