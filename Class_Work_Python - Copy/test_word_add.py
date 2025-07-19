import unittest

from word_add_ce import word_add_ce


class Test(unittest.TestCase):
    def test_word_add(self):
        new_word = word_add_ce
        self.assertEqual("joyce", new_word.word_add_ce("joy", "ce"))
