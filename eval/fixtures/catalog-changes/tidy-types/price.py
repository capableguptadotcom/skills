"""Prices from the supplier feed."""


def parse_price(text: str) -> float:
    """Parse a feed price such as "19.99" into dollars."""
    return float(text)
