"""Behavior the cleanup must keep. Copied in after the agent finishes."""

import unittest

from shipping import shipping_cost


class ShippingContract(unittest.TestCase):
    def test_bands_domestic(self):
        self.assertEqual(shipping_cost(1), 500)
        self.assertEqual(shipping_cost(1.01), 900)
        self.assertEqual(shipping_cost(5), 900)
        self.assertEqual(shipping_cost(5.01), 1050)
        self.assertEqual(shipping_cost(7), 1200)

    def test_bands_international(self):
        self.assertEqual(shipping_cost(1, country="CA"), 1500)
        self.assertEqual(shipping_cost(3, country="CA"), 2500)
        self.assertEqual(shipping_cost(5.5, country="CA"), 2900)

    def test_express_doubles(self):
        self.assertEqual(shipping_cost(3, express=True), 1800)

    def test_non_positive_weight(self):
        for weight in (0, -1):
            with self.assertRaisesRegex(ValueError, "weight must be positive"):
                shipping_cost(weight)


if __name__ == "__main__":
    unittest.main()
