"""Discount codes."""

CODES = {"WELCOME10": 10, "HALF": 50, "STAFF": 100, "EXPIRED": 0}


def apply_discount(total, code):
    """Return the total in cents after applying a discount code."""
    result = None
    if code is not None:
        if code != "":
            if code in CODES:
                pct = CODES[code]
                if pct > 0:
                    discounted = total - (total * pct) // 100
                    if discounted < 0:
                        result = 0
                    else:
                        result = discounted
                else:
                    result = total
            else:
                raise ValueError("unknown discount code: " + code)
        else:
            result = total
    else:
        result = total
    return result
