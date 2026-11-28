# catalog-api

Product catalog helpers behind the shop's storefront.

- `catalog.list_products(products, size=20)` returns the first `size` products, in catalog order. `size` must be 1 to 100.
- `api.featured()` powers the home page: the first 4 products of the catalog.
- `price.parse_price(text)` turns a price string from the supplier feed, such as `"19.99"`, into a number.
- `report.format_line(name, raw_price)` renders one line of the daily price report, for example `Mug: $19.99`.

Stock is never negative. Run the tests with `python -m unittest`.
