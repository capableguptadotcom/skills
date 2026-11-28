"""Product catalog queries."""


def list_products(products, size=20, in_stock_only=False):
    """Return the first `size` products in catalog order.

    With `in_stock_only`, products whose stock is 0 are left out before the first `size` are taken.
    """
    if not 1 <= size <= 100:
        raise ValueError("size must be between 1 and 100")
    if in_stock_only:
        products = [p for p in products if p["stock"] > 0]
    return products[:size]
