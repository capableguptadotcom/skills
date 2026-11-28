"""Cart quantities."""


def parse_quantity(value):
    if isinstance(value, bool):
        raise TypeError("quantity must be an integer, not bool")
    if isinstance(value, int):
        if value < 1:
            raise ValueError("quantity must be at least 1")
        else:
            return value
    else:
        if isinstance(value, str):
            stripped = value.strip()
            if stripped.isdigit():
                number = int(stripped)
                if number < 1:
                    raise ValueError("quantity must be at least 1")
                else:
                    return number
            else:
                raise ValueError("quantity must be a whole number")
        else:
            raise TypeError("quantity must be an integer")
