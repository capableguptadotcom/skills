import unittest

from discounts import apply_discount
from quantity import parse_quantity
from receipt import receipt_lines


class DiscountTest(unittest.TestCase):
    def test_welcome_code(self):
        self.assertEqual(apply_discount(1000, "WELCOME10"), 900)

    def test_no_code(self):
        self.assertEqual(apply_discount(1000, None), 1000)


class QuantityTest(unittest.TestCase):
    def test_int(self):
        self.assertEqual(parse_quantity(3), 3)

    def test_string(self):
        self.assertEqual(parse_quantity("2"), 2)


class ReceiptTest(unittest.TestCase):
    def test_line(self):
        self.assertEqual(receipt_lines([{"qty": 2, "name": "Mug", "unit_cents": 1250}]), ["2 x Mug  $25.00"])


if __name__ == "__main__":
    unittest.main()
