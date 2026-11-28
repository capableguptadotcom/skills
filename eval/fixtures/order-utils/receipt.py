"""Printed receipts."""


def format_cents(cents):
    return f"${cents // 100}.{cents % 100:02d}"


def receipt_lines(items):
    """One line per item: quantity, name and line total."""
    return [f"{item['qty']} x {item['name']}  {format_cents(item['qty'] * item['unit_cents'])}"
            for item in items]
