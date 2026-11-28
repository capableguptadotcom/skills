# catalog-api

Product catalog helpers behind the shop's storefront.

- `catalog.list_products(products, size=20, in_stock_only=False)` returns the first `size` products, in catalog order. `size` must be 1 to 100. With `in_stock_only=True`, products with stock 0 are left out.
- `api.featured()` powers the home page: the first 4 products of the catalog.
- `price.parse_price(text)` turns a price string from the supplier feed, such as `"19.99"`, into a number.
- `report.format_line(name, raw_price)` renders one line of the daily price report, for example `Mug: $19.99`.

Stock is never negative. Run the tests with `python -m unittest`.
