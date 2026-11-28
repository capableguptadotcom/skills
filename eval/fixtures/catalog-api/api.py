"""Storefront endpoints."""

from catalog import list_products

PRODUCTS = [
    {"sku": f"SKU-{n:03d}", "name": f"Product {n}", "stock": n % 3}
    for n in range(1, 61)
]


def featured():
    """The home page shows the first four products of the catalog."""
    return [p["name"] for p in list_products(PRODUCTS, size=4)]
