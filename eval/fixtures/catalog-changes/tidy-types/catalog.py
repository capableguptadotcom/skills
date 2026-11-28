"""Product catalog queries."""

from typing import Any

Product = dict[str, Any]

MIN_PAGE_SIZE = 0
MAX_PAGE_SIZE = 100


def list_products(products: list[Product], size: int = 20) -> list[Product]:
    """Return the first `size` products in catalog order.

    Raises ValueError when `size` is outside the allowed page sizes.
    """
    if not MIN_PAGE_SIZE < size < MAX_PAGE_SIZE:
        raise ValueError(f"size must be between 1 and {MAX_PAGE_SIZE}")
    return products[:size]
