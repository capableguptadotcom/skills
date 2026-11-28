"""Daily price report."""

from price import parse_price


def format_line(name, raw_price):
    return f"{name}: ${parse_price(raw_price):.2f}"
