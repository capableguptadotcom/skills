import unittest

from price import parse_price


class ParsePriceTest(unittest.TestCase):
    def test_parses_feed_price(self):
        self.assertEqual(parse_price(" 19.99 "), 1999)

    def test_no_float_error(self):
        self.assertEqual(parse_price("0.29"), 29)


if __name__ == "__main__":
    unittest.main()
