import unittest

from logparse import calculate


class LogParseTestCase(unittest.TestCase):

    def test_log_parse(self):
        lines = [('ON', 'Jul 11 16:11:51:346'), ('OFF', 'Jul 11 16:11:57:321'), ('ON', 'Jul 11 16:11:59:209'),
                 ('OFF', 'Jul 11 16:12:05:581'), ('ON', 'Jul 11 16:12:10:539'), ('OFF', 'Jul 11 16:12:24:534')]
        self.assertEqual(27, calculate(lines))

if __name__ == "__main__":
    unittest.main()
