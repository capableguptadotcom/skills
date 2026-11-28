# Orders page

The orders page loads a customer's orders and shows one status line above the list.

State lives in `src/orderState.ts`. `src/OrdersPanel.tsx` renders it.

Tests run on Node's built-in type stripping, so use only erasable TypeScript syntax (no `enum`, no `namespace`, no parameter properties):

```sh
node --experimental-strip-types --test "test/*.test.ts"
```
