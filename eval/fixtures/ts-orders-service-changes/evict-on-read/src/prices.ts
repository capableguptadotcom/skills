import { TtlCache } from "./cache.ts";

const cache = new TtlCache<number>(60_000);

export async function priceFor(sku: string, lookup: (sku: string) => Promise<number>): Promise<number> {
  const cached = cache.get(sku);
  if (cached !== undefined) return cached;
  const price = await lookup(sku);
  cache.set(sku, price);
  return price;
}

export function cachedPriceCount(): number {
  return cache.size();
}
