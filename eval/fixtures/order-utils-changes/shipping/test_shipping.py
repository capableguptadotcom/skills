import unittest

from shipping import shipping_cost


class ShippingTest(unittest.TestCase):
    def test_small_domestic(self):
        self.assertEqual(shipping_cost(0.5), 500)

    def test_heavy_international_express(self):
        self.assertEqual(shipping_cost(6.2, express=True, country="DE"), 2 * (2500 + 2 * 400))


if __name__ == "__main__":
    unittest.main()
