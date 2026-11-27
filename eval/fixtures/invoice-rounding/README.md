# Invoices

Amounts are integer cents. A line's discount is applied to the line total and rounded to the nearest cent, halves rounded up, which matches the point-of-sale system's receipts. `format_money` only formats; it never rounds.

Run the tests with `python -m unittest`.
