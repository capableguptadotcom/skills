"""Daily price report."""

from price import parse_price


def format_line(name: str, raw_price: str) -> str:
    """One line of the daily report, for example "Mug: $19.99"."""
    dollars = parse_price(raw_price)
    return f"{name}: ${dollars:.2f}"
