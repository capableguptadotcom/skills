"""Product catalog queries."""


def list_products(products, page=1, size=20):
    """Return one page of products in catalog order. Pages are numbered from 1."""
    if not 1 <= size <= 100:
        raise ValueError("size must be between 1 and 100")
    start = page * size
    return products[start:start + size]
