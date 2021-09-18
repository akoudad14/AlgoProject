import unittest

from keypad_string import keypad_string


class KeypadStringTestCase(unittest.TestCase):

    def test_keypad1(self):
        self.assertEqual('adgj', keypad_string('12345'))

    def test_keypad2(self):
        self.assertEqual('hello', keypad_string('4433555555666'))

    def test_keypad3(self):
        self.assertEqual('a  b', keypad_string('20022'))

    def test_keypad4(self):
        self.assertEqual('', keypad_string(''))

    def test_keypad5(self):
        self.assertEqual('', keypad_string('111'))


if __name__ == "__main__":
    unittest.main()
