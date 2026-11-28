"""Storefront endpoints."""

from catalog import Product, list_products

FEATURED_COUNT = 4

PRODUCTS: list[Product] = [
    {"sku": f"SKU-{number:03d}", "name": f"Product {number}", "stock": number % 3}
    for number in range(1, 61)
]


def featured() -> list[str]:
    """The home page shows the first four products of the catalog."""
    return [product["name"] for product in list_products(PRODUCTS, size=FEATURED_COUNT)]
