export type Lease = { owner: string; expiresAt: number };

// A thin wrapper over Redis. Each method is one network round trip.
export interface LeaseStore {
  get(key: string): Promise<Lease | undefined>;
  set(key: string, lease: Lease): Promise<void>;
  // SET key value NX PX ttl: stores the lease only if the key does not exist, true when it did.
  setIfAbsent(key: string, lease: Lease, ttlMs: number): Promise<boolean>;
  delete(key: string): Promise<void>;
}
