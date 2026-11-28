"""Prices from the supplier feed."""

from decimal import Decimal


def parse_price(text):
    """Parse a feed price such as "19.99" into integer cents, avoiding float rounding."""
    return int(Decimal(text.strip()) * 100)
