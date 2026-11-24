# Lease service
A single event loop serves lease claims. At most one worker may receive a successful claim for the same initially free lease. A failed claim returns False. The refactor adds a checkpoint used by the transport adapter.

Run existing verification with `python verification/model.py`. `verification/checks.json` records individual correspondence anchors. The archive audit command is not installed on this workstation.
