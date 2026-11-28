# order-utils

Helpers for the checkout service. Amounts are integer cents.

- `discounts.apply_discount(total, code)`: no code (None or "") leaves the total unchanged; an unknown code is an error the checkout shows to the customer.
- `quantity.parse_quantity(value)`: accepts a positive int, or a string of digits with optional surrounding spaces, from the cart form.
- `receipt.receipt_lines(items)`: one line per item, for the printed receipt.

Run the tests with `python -m unittest`.
