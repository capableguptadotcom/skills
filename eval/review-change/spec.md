# review-change: specification

**Job.** Report what is wrong with a bounded change, with evidence, and edit nothing.

**Output.** Findings ranked by impact, each with a reachable trigger, the wrong outcome and a location; what the review could not cover. "No findings" is a valid result.

**Must.**

- Bound the review to the change asked about (a branch against its base, a commit).
- Check the change against what defines correct: the README or requirement, the changed callers, the tests.
- Find defects that reach outside the diff, such as an unchanged caller the change breaks.
- Leave every file unchanged.

**Must not.**

- Invent findings on a correct change, or present style or speculation as a defect.
- Treat passing tests as proof when they do not cover the changed behavior.
- Review the whole repository instead of the change.

**Hosts.** Claude Code and Codex.

**Triggers.** "review this branch", "review my last commit", "look over this PR".
**Near misses.** Fixing a known bug; simplifying code; designing before code exists.

**Cases.** See `cases.json`. All three use `eval/fixtures/catalog-api` with a change from `eval/fixtures/catalog-changes` committed on a `feature` branch:

- `pagination-off-by-one`: page numbers are 1-based in the README, but `start = page * size`, so the default page 1 skips the first page and the unchanged home-page caller `api.featured()` shows products 5 to 8 instead of 1 to 4. The new tests check only lengths and pass.
- `cents-breaks-caller`: `parse_price` now returns integer cents and its tests were updated, but the unchanged `report.format_line` still formats the result as dollars (`$1999.00`). No test covers the report.
- `clean-filter`: a correct `in_stock_only` filter with tests. The trap is inventing defects.
