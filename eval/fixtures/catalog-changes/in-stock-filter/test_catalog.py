import unittest

from catalog import list_products


def make(n):
    return [{"sku": f"SKU-{i:03d}", "name": f"Product {i}", "stock": 1} for i in range(1, n + 1)]


class ListProductsTest(unittest.TestCase):
    def test_default_size(self):
        self.assertEqual(len(list_products(make(50))), 20)

    def test_rejects_bad_size(self):
        with self.assertRaises(ValueError):
            list_products(make(5), size=0)

    def test_in_stock_only_skips_sold_out(self):
        products = make(4)
        products[0]["stock"] = 0
        products[2]["stock"] = 0
        names = [p["name"] for p in list_products(products, size=2, in_stock_only=True)]
        self.assertEqual(names, ["Product 2", "Product 4"])

    def test_default_keeps_sold_out(self):
        products = make(3)
        products[0]["stock"] = 0
        self.assertEqual(len(list_products(products)), 3)


if __name__ == "__main__":
    unittest.main()
