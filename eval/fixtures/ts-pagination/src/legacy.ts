// Old search adapter, kept until the search team migrates (tracked elsewhere).
export function normalizeHit(hit: any) {
  return { id: hit.objectID as string, title: (hit.title || "").trim(), price: hit.price_cents / 100 };
}
