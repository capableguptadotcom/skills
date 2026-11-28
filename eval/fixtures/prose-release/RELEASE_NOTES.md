# Release 3.4.0

## Highlights

It is with great excitement that we unveil version 3.4.0, a pivotal release that truly elevates the sync experience to new heights. In order to provide maximum clarity, we have carefully crafted these notes to walk you through every enhancement.

## Fixed: uploads stalling on large folders

Additionally, we have addressed an issue where, in some cases, uploads of folders with more than 10,000 files could potentially stall indefinitely. If you previously saw the following error, it is now resolved:

```
SyncError: crucial manifest chunk missing — retry budget exhausted (code E_MANIFEST_42)
```

## Changed: config location

The configuration file has moved, serving as a testament to our commitment to following platform conventions. Run the migration once:

```sh
sync migrate-config --from ~/.syncrc --to ~/.config/sync/config.toml
```

One beta tester summed it up: "the folder that used to hang for an hour now finishes in four minutes."

## Removed

Support for the legacy `--fast` flag has been removed, as it was deprecated in 3.1.0.
