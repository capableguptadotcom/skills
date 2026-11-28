# Nightly export worker

Two worker pods run `runNightlyExport` (`src/worker.ts`) from a cron at 02:00. Only one may export at a time: two exports at once write the same files in the data bucket and corrupt them. The lease lives in Redis (`src/store.ts`).
