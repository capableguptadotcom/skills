"""Product catalog queries."""


def list_products(products, size=20):
    """Return the first `size` products in catalog order."""
    if not 1 <= size <= 100:
        raise ValueError("size must be between 1 and 100")
    return products[:size]
