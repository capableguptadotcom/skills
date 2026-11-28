import unittest

from money import format_money, invoice_total, line_total


class MoneyTests(unittest.TestCase):
    def test_line_without_discount(self):
        self.assertEqual(line_total(1000, 2), 2000)

    def test_line_with_even_discount(self):
        self.assertEqual(line_total(1000, 1, 15), 850)

    def test_invoice_total(self):
        lines = [{"price_cents": 1000, "qty": 2}, {"price_cents": 500, "qty": 1, "discount_pct": 10}]
        self.assertEqual(invoice_total(lines), 2450)

    def test_format_money(self):
        self.assertEqual(format_money(2450), "24.50")
        self.assertEqual(format_money(5), "0.05")


if __name__ == "__main__":
    unittest.main()
