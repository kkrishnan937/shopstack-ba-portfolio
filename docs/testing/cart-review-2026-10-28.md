# Cart implementation review and verification

**28 October 2026 (America/Regina); CI timestamps are 29 October UTC.**

The read-only cart slice now passes the same 15 automated acceptance checks on local Edge/PGlite and in CI on both embedded PostgreSQL and a PostgreSQL 17 server. This is actual execution evidence, not independent customer UAT or release approval.

## Changes found during review

- A failed catalog response could reach `products.map` and crash the cart page. The client now validates the response; a controlled catalog failure verifies that cart viewing still works without an uncaught browser error.
- An aborted cart request now stops before processing a late authentication response.
- Price-notice absence is checked in each relevant read-only state.
- The first CI embedded run exposed a missing database parent directory when evidence was written elsewhere. The harness now creates its run directory independently; the rerun passed.
- A separate pull-request workflow builds and tests both database adapters without cloud deployment permissions or AWS credentials.

## Evidence and scope

[Successful CI run](https://github.com/kkrishnan937/shopstack/actions/runs/40808158396), source commit `de1ca0ef95b3d5f456f8aa2034e78318cda9fb73`, [follow-up PR #2](https://github.com/kkrishnan937/shopstack/pull/2).

| Execution | Outcome | Durable evidence |
|---|---|---|
| Local Microsoft Edge, file-backed PGlite | 15 Pass | [Results](evidence/cart-review-2026-10-28/run-results.json) |
| CI Chromium, file-backed PGlite | 15 Pass | [Results](evidence/cart-review-ci-embedded-2026-10-28/run-results.json) |
| CI Chromium, PostgreSQL 17 | 15 Pass | [Results](evidence/cart-review-postgres-2026-10-28/run-results.json) |

These are repeated executions of **9 planned test families plus 6 supplemental checks**, not 45 distinct requirements. The other 28 planned families remain Not run. Supplemental checks cover authentication/write gates, session expiry, mobile overflow, ownership, persistence and catalog failure.

Each evidence folder includes screenshots, API output, before/after saved-state snapshots and a source/build manifest. PostgreSQL persistence was verified after closing and reopening the application connection pool, not restarting the database server. Embedded persistence was verified by closing and reopening its database. Only isolated synthetic fixtures were used.

Downloaded CI ZIP SHA-256 checks matched GitHub's artifact digests:

- PostgreSQL: `572d107724fde358946b2dea81a4e3d3dde34fbc1ad3b772ff7d89bbe24035a2`.
- Embedded: `1dd2986c738519408651ea47d688de521822949a5bfa542a121c806256c09f4e`.

## Delivery position

The repository owner merged [initial PR #1](https://github.com/kkrishnan937/shopstack/pull/1) during this review. Its existing [main deployment workflow](https://github.com/kkrishnan937/shopstack/actions/runs/40807617236) passed its test job, failed while configuring AWS credentials and skipped deployment. No successful production deployment is evidenced.

PR #2 remains a draft for review. A human cart walkthrough and independent business acceptance are still outstanding. The legacy cart-age policy starts retention when missing historical metadata is first initialized; it remains an explicit migration tradeoff. Exact retention-boundary testing, full accessibility, cart mutations, logout invalidation and prolonged mutation recovery are outside this verified slice.

The next BA task is to observe the human walkthrough, record actual results and any defects, then review acceptance and outstanding release gates with the decision maker.
