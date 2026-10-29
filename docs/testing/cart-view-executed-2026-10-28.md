# Executed cart-viewing acceptance run

**Local date:** 28 October 2026, America/Regina  
**Run:** 2026-10-29T02-21-37-090Z (UTC; 28 October at 8:21 p.m. Regina)  
**Result:** 9 planned test families Pass; 5 supplemental checks Pass  
**Execution:** Agent-driven automated browser acceptance checks; not independent business sign-off

## Build and environment

Uploaded implementation: [draft pull request](https://github.com/kkrishnan937/shopstack/pull/1) and [tested source revision](https://github.com/kkrishnan937/shopstack/tree/292b65e396db295763ef07cc109c324c7ca787ca). Review/merge/deployment are separate from this local execution.

Application source commit: `292b65e396db295763ef07cc109c324c7ca787ca`, local branch `codex/cart-viewing-slice`. This commit records the already-executed source; no implementation source changed between the final run and that commit. Build fingerprint: `8366153a9da11ad2c05a73ae6caf1bd2fe1fae09a55d1b614bf9892f131a26e6`. [SHA-256 manifest](evidence/cart-view-2026-10-28/build-manifest.json) identifies exact tested files and built assets.

Node v24.22.1, pinned PGlite 0.3.14 with a unique file-backed database, actual Express backend and authentication routes, actual Vite production build served through Express on an ephemeral loopback port, and headless Microsoft Edge. No browser-route response mocks. This is a real local SQL-backed application run, not the wireframe, but not a conventional deployed PostgreSQL server environment. Full production integration remains unverified.

Frontend build completed successfully. The test harness generated synthetic credentials in memory, seeded only its isolated database and logged in through the real UI. Credentials/tokens are absent from published evidence. The test-only injected hook failed the authenticated cart read; it did not replace the API response in the browser or disable login.

## Primary executed case: failure, retry and recovery

Preconditions actually established: valid synthetic login; two Coffee Mugs at CAD 12.50 and one Wireless Mouse at CAD 24.99; subtotal CAD 49.99; last successful change 20 days earlier; current prices unchanged; no in-flight mutation. Backend failure control applied only to cart reads.

| Step | Expected | Actual recorded result | Evidence |
|---|---|---|---|
| Select View cart with failure enabled | Error and Retry, without empty/zero claim | GET returned 503; correct message and Retry displayed; no Cart is empty or subtotal displayed; saved items/metadata unchanged. Pass. | [Initial failure screenshot](evidence/cart-view-2026-10-28/01-cart-load-failure.png) |
| Select Retry with failure still enabled | Another non-mutating read; error remains | Another GET returned 503; error/Retry remained; saved items and retention timestamp unchanged. Pass. | [Repeated failure screenshot](evidence/cart-view-2026-10-28/02-retry-still-failing.png) |
| Remove failure control and select Retry | Successful saved cart retrieval | GET returned 200; quantities 2 and 1; lines CAD 25.00 / CAD 24.99; subtotal CAD 49.99; error cleared. Pass. | [Recovered cart screenshot](evidence/cart-view-2026-10-28/03-cart-recovered.png), [API response](evidence/cart-view-2026-10-28/cart-response.json) |
| Compare before/after saved state | No item/version/retention changes from read/retry | Direct database snapshots matched. Only GET cart requests occurred in the failure/recovery sequence. Pass. | [Before](evidence/cart-view-2026-10-28/saved-state-before.json), [after](evidence/cart-view-2026-10-28/saved-state-after.json), [request/status log](evidence/cart-view-2026-10-28/run-results.json) |

**Disposition:** CART-T-04 and CART-T-05 now Pass in this identified local environment. BLK-CART-01 is resolved for this slice/environment, not deleted from history or declared resolved in production.

## Other actual results

| Test | Actual outcome | Result |
|---|---|---|
| CART-T-01 | Names, quantities, API-provided integer-cent unit/line/subtotal amounts matched the signed-in fixture and rendered cart. | Pass |
| CART-T-02 | Two mugs and one mouse produced 2500 + 2499 = 4999 cents, displayed CAD 49.99. | Pass |
| CART-T-03 | Controlled empty fixture showed Cart is empty, CAD 0.00 and continuation; no expiry notice. | Pass |
| CART-T-06 | Continue shopping navigated to catalog from both active and empty carts; saved data was unchanged by navigation. | Pass |
| CART-T-07 | Cart-only subtotal/checkout-policy/no-payment notice appeared in implemented active, error, empty and expired states. Screenshots support state coverage; checkout itself is not implemented. | Pass |
| CART-T-28 | Fixture aged 721 hours was expired by the backend; items deleted, zero displayed, reason persisted. View-local dismissal did not clear server reason; next view restored notice. Exact boundary was not tested. | Pass |
| CART-T-29 | Day-20 active reads preserved the original saved retention timestamp. | Pass |
| SUP-AUTH-WRITES | Unauthenticated cart read returned 401; cart POST/DELETE and order POST returned 501, with fixture unchanged. | Pass |
| SUP-SESSION | Expired token caused sign-in feedback, no cart subtotal/expiry claim from authentication failure, and no persisted-cart change. | Pass |
| SUP-MOBILE | Expired cart at 320px had no horizontal overflow. This is not a complete mobile/accessibility audit. | Pass |
| SUP-OWNERSHIP | Another synthetic customer's quantity-7 line was not exposed; that record remained unchanged. | Pass |
| SUP-PERSIST | Original fixture was restored after state-specific tests, database closed/reopened from disk, and quantities 2/1 were still persisted. | Pass |

## Evidence, cleanup and limits

[Machine-readable assertions/results](evidence/cart-view-2026-10-28/run-results.json), [empty screenshot](evidence/cart-view-2026-10-28/04-empty-cart.png), [expired screenshot](evidence/cart-view-2026-10-28/05-expired-cart.png), [session-expiry screenshot](evidence/cart-view-2026-10-28/06-session-expired.png), [mobile screenshot](evidence/cart-view-2026-10-28/07-mobile-cart.png).

Fixture deletes/age changes between state-specific cases were explicit direct SQL test setup, not customer/API mutations. Before/after snapshots refer specifically to the primary active-cart failure/retry sequence. The harness restored that fixture for its persistence check, closed the browser/server/database, and retained the unique ignored synthetic database directory. No production data was used or altered. Failure injection ceased with the isolated harness; there is no public failure toggle.

The complete suite has 9 Pass and 28 Not run planned families, plus 5 separate supplemental checks. No required mutation scenario is claimed passed. Legacy cart timestamps were unavailable, so new metadata begins legacy retention on first migration read; this tradeoff needs review before release. Versions, variants, price notices, safe mutation reconciliation, logout revocation, exact retention boundary and checkout remain incomplete or untested. No full-release acceptance or security/compliance conclusion follows.

Reproduce with the application's `docs/cart-viewing-run.md` and `backend/test/cart-view.e2e.cjs`. Code/test harness belongs in the application repository; this portfolio retains results and analysis rather than duplicate implementation scripts.
