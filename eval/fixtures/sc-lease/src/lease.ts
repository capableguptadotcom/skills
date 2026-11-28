import type { LeaseStore } from "./store.ts";

export async function tryAcquire(store: LeaseStore, key: string, workerId: string, ttlMs: number, now = Date.now()) {
  const current = await store.get(key);
  if (current && current.expiresAt > now && current.owner !== workerId) return false;
  await store.set(key, { owner: workerId, expiresAt: now + ttlMs });
  return true;
}
