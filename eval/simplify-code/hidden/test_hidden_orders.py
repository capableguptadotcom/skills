"""Behavior the cleanup must keep. Copied in after the agent finishes."""

import unittest

from discounts import apply_discount
from quantity import parse_quantity
from receipt import receipt_lines


class DiscountContract(unittest.TestCase):
    def test_empty_code_keeps_total(self):
        self.assertEqual(apply_discount(1000, ""), 1000)

    def test_zero_percent_code_keeps_total(self):
        self.assertEqual(apply_discount(999, "EXPIRED"), 999)

    def test_floor_division_kept(self):
        self.assertEqual(apply_discount(999, "HALF"), 500)

    def test_full_discount_is_zero(self):
        self.assertEqual(apply_discount(1234, "STAFF"), 0)

    def test_unknown_code_message(self):
        with self.assertRaisesRegex(ValueError, r"^unknown discount code: NOPE$"):
            apply_discount(1000, "NOPE")

    def test_codes_are_case_sensitive(self):
        with self.assertRaises(ValueError):
            apply_discount(1000, "welcome10")


class QuantityContract(unittest.TestCase):
    def test_bool_rejected(self):
        with self.assertRaisesRegex(TypeError, "not bool"):
            parse_quantity(True)

    def test_float_rejected(self):
        with self.assertRaises(TypeError):
            parse_quantity(2.0)

    def test_plus_sign_rejected(self):
        with self.assertRaisesRegex(ValueError, "whole number"):
            parse_quantity("+3")

    def test_negative_string_rejected(self):
        with self.assertRaisesRegex(ValueError, "whole number"):
            parse_quantity("-1")

    def test_spaces_allowed(self):
        self.assertEqual(parse_quantity(" 4 "), 4)

    def test_zero_rejected(self):
        with self.assertRaisesRegex(ValueError, "at least 1"):
            parse_quantity("0")
        with self.assertRaisesRegex(ValueError, "at least 1"):
            parse_quantity(0)

    def test_none_rejected(self):
        with self.assertRaises(TypeError):
            parse_quantity(None)


class ReceiptContract(unittest.TestCase):
    def test_cents_padding(self):
        self.assertEqual(receipt_lines([{"qty": 1, "name": "Pen", "unit_cents": 105}]), ["1 x Pen  $1.05"])

    def test_empty(self):
        self.assertEqual(receipt_lines([]), [])


if __name__ == "__main__":
    unittest.main()
