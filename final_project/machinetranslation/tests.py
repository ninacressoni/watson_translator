import unittest
from translator import english_to_french, french_to_english

class LanguageTranslator(unittest.TestCase):
    def test_en_to_fr(self):
        self.assertNotEqual(english_to_french("None"), "")
        self.assertNotEqual(english_to_french(0), 0)
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_fr_to_en(self):
        self.assertNotEqual(french_to_english("None"), "")
        self.assertNotEqual(french_to_english(0), 0)
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()