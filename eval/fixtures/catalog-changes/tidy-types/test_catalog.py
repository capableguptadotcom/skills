import unittest

from catalog import Product, list_products


def make(n: int) -> list[Product]:
    return [{"sku": f"SKU-{i:03d}", "name": f"Product {i}", "stock": 1} for i in range(1, n + 1)]


class ListProductsTest(unittest.TestCase):
    def test_default_size(self):
        self.assertEqual(len(list_products(make(50))), 20)

    def test_rejects_bad_size(self):
        with self.assertRaises(ValueError):
            list_products(make(5), size=0)

    def test_small_page(self):
        self.assertEqual(len(list_products(make(5), size=3)), 3)


if __name__ == "__main__":
    unittest.main()
