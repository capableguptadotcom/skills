# 3 November: ledger total showed "01200"

During a sandbox test the provider sent `"amount_cents": "1200"` (a string). The webhook recorded it, and the ledger's USD total became the string `"01200"`, which the finance export then rejected. We deleted the bad entry by hand.
