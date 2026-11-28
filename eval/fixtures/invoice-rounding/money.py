"""Invoice arithmetic. All amounts are integer cents."""


def line_total(price_cents, qty, discount_pct=0):
    """Total for one invoice line after its percentage discount."""
    gross = price_cents * qty
    return gross * (100 - discount_pct) // 100


def invoice_total(lines):
    return sum(line_total(**line) for line in lines)


def format_money(cents):
    """Format non-negative cents as '12.34'."""
    return f"{cents // 100}.{cents % 100:02d}"
