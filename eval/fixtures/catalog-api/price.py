"""Prices from the supplier feed."""


def parse_price(text):
    """Parse a feed price such as "19.99" into dollars."""
    return float(text.strip())
