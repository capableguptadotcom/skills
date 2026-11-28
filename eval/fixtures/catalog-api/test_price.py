import unittest

from price import parse_price


class ParsePriceTest(unittest.TestCase):
    def test_parses_feed_price(self):
        self.assertEqual(parse_price(" 19.99 "), 19.99)


if __name__ == "__main__":
    unittest.main()
