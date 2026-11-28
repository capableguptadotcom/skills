// Price lookups are slow, so the dashboard caches them for a minute.
// The cache holds at most a few hundred SKUs (one per catalog item shown on a page).
export class TtlCache<V> {
  private entries = new Map<string, { value: V; expiresAt: number }>();
  private readonly ttlMs: number;
  private readonly now: () => number;

  constructor(ttlMs: number, now: () => number = Date.now) {
    this.ttlMs = ttlMs;
    this.now = now;
  }

  get(key: string): V | undefined {
    this.evictExpired();
    const entry = this.entries.get(key);
    if (!entry || entry.expiresAt <= this.now()) return undefined;
    return entry.value;
  }

  set(key: string, value: V): void {
    this.entries.set(key, { value, expiresAt: this.now() + this.ttlMs });
  }

  // Removes only entries whose time is up. get() already treats those as missing.
  evictExpired(): void {
    const now = this.now();
    for (const [key, entry] of this.entries) {
      if (entry.expiresAt <= now) this.entries.delete(key);
    }
  }

  size(): number {
    return this.entries.size;
  }
}
