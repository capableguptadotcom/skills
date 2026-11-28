import type { LeaseStore } from "./store.ts";
import { tryAcquire } from "./lease.ts";

export async function runNightlyExport(store: LeaseStore, workerId: string, exportAll: () => Promise<void>) {
  if (!(await tryAcquire(store, "nightly-export", workerId, 15 * 60_000))) return "skipped";
  try {
    await exportAll(); // takes 5 to 10 minutes
  } finally {
    await store.delete("nightly-export");
  }
  return "exported";
}
