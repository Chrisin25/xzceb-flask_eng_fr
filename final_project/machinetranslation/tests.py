import unittest
from translator import english_to_french,french_to_english

class TestengTofre(unittest.TestCase):
    def test1(self):self.assertEqual(english_to_french(""), "Null Input")
    def test2(self):self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestfreToeng(unittest.TestCase):
    def test1(self):self.assertEqual(french_to_english(""), "Null Input")
    def test2(self):self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
