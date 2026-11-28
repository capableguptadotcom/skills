# Payments webhook

`src/webhook.ts` receives the payment provider's webhook (the API route passes it the raw request body) and records succeeded payments in the ledger (`src/ledger.ts`). The provider's payload contract is in `docs/provider.md`.

Tests run on Node's built-in type stripping, so use only erasable TypeScript syntax (no `enum`, no `namespace`, no parameter properties):

```sh
node --experimental-strip-types --test "test/*.test.ts"
```
