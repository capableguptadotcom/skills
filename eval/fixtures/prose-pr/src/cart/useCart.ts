export function useCart() {
  // Cart v2: one request per checkout instead of one per line item.
  return { lines: [] as { sku: string; qty: number }[] };
}
