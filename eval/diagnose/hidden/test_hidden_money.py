"""Hidden acceptance test: discounts round to the nearest cent, halves up."""

import unittest

from money import format_money, invoice_total, line_total


class HiddenMoneyTests(unittest.TestCase):
    def test_half_cent_rounds_up(self):
        self.assertEqual(line_total(333, 1, 50), 167)

    def test_below_half_rounds_down(self):
        self.assertEqual(line_total(999, 1, 15), 849)

    def test_above_half_rounds_up(self):
        self.assertEqual(line_total(1999, 3, 15), 5097)

    def test_unchanged_cases(self):
        self.assertEqual(line_total(1000, 2), 2000)
        self.assertEqual(invoice_total([{"price_cents": 333, "qty": 1, "discount_pct": 50},
                                        {"price_cents": 1000, "qty": 1}]), 1167)

    def test_format_money_unchanged(self):
        self.assertEqual(format_money(1167), "11.67")
        self.assertEqual(format_money(5), "0.05")


if __name__ == "__main__":
    unittest.main()
