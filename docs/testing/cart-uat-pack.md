# Cart UAT test pack

**Version:** 0.1  
**Prepared:** 28 October 2026  
**Status:** Draft for business, technical and test review; no acceptance scenarios completed

## Scope, references and execution controls

Expands the [37 planned outlines](../requirements/cart-traceability-matrix.md) for [requirements v0.3](../requirements/cart-requirements.md). CART-T-11 has its detailed procedure in [CART-UAT-01 v0.2](quantity-update-uat-case.md); the other 36 outlines are expanded here. These are draft procedures, not executed results. Scenario families with multiple variants need a separate execution record per variant. No baseline approval, technical feasibility or customer acceptance is implied.

The [actual readiness inspection](cart-loading-readiness-2026-10-28.md) blocked CART-T-04 and CART-T-05 before scenario execution. That recorded status is preserved. Other outlines remain Not run; this does not assert they are ready. Missing implementation and environment prerequisites must be checked before each execution. Recovery and logout cases also need decisions before expected behaviour can be baselined.

The business reviewer validates customer outcomes; developer/tester assistance is needed for controlled failures, request tracking, clock manipulation and persisted-data evidence. Do not require business reviewers to inject failures or inspect databases themselves. Perform technical supporting checks in an isolated test environment and connect their evidence to the business scenario.

## Shared setup and fixtures

Before each case:

1. Identify the application build, test environment, reviewer/tester and requirement/case version. Confirm synthetic accounts, authorization and relevant features exist.
2. Reset only the owned synthetic fixture through an agreed, safe method. Verify starting saved data, current prices and retention timestamps. No other session or unresolved request changes the cart unless a case explicitly requires it.
3. Authenticate the synthetic customer with valid credentials unless the scenario concerns logout. Never publish credentials, tokens or full unsanitized network captures.
4. Disable failure controls except those explicitly required. Record how to enable, remove and verify cleanup of a controlled failure; keep authentication and unrelated requests unaffected.
5. Use agreed UI and technical evidence to verify saved-state changes or non-mutation. A screen refresh alone is not proof of persistence. Apply CART-UAT-01's authorized-alternative and partial-result policy; do not bypass access restrictions.

| Fixture | Starting saved cart | Subtotal |
|---|---|---|
| F1 | Only 2 mugs, same identified product/variant, CAD 12.50 each | CAD 25.00 |
| F2 | 2 mugs at CAD 12.50 each and 1 mouse at CAD 24.99 | CAD 49.99 |
| F0 | No saved items; valid active customer | CAD 0.00 |
| F10 | 10 identical mugs at CAD 12.50 each | CAD 125.00 |

Unless stated otherwise, use active non-expired carts and unchanged prices. Money is CAD with two decimal places. Map exact fixture identities to the execution record rather than assuming product names uniquely identify database rows.

## Execution record template

Create a record per test and variant; do not overwrite earlier evidence during a rerun.

| Field | Value to fill during execution |
|---|---|
| Test / variant / case version | |
| Requirement version / build / environment | |
| Execution date and tester / business reviewer | |
| Synthetic fixture and verified preconditions | |
| Controlled setup and technical support | |
| Per-step actual results and evidence | |
| Overall status and rationale | |
| Defect / blocker reference | |
| Cleanup verification and retest reference | |

For the procedures below, expected results are not actual results. Preserve results for each numbered action, including technical support observations. Not run means no execution; Blocked means a prerequisite prevented an attempted case from proceeding. Fail requires an observed contradiction of an agreed expectation. Pass requires all mandatory checks and evidence. Known failures must not be hidden by another blocked check. If a mandatory check is unavailable, use the partial-result rules in CART-UAT-01 rather than silently marking the full case Pass.

## Cart review and navigation

| Test / criterion | Setup and procedure | Expected result | Status | Actual / evidence |
|---|---|---|---|---|
| CART-T-01 / CART-AC-01 | F1. 1. Open View cart. 2. Compare each visible field with the fixture and saved read. | Mug name/variant as designed, quantity 2, unit CAD 12.50, line/subtotal CAD 25.00. Values belong to the signed-in customer's cart. | Not run | |
| CART-T-02 / CART-AC-02 | F2. 1. Open cart. 2. Verify both lines and independently calculate each amount. | Mug line CAD 25.00; mouse line CAD 24.99; subtotal CAD 49.99. | Not run | |
| CART-T-03 / CART-AC-03 | F0. 1. Open cart. 2. Confirm retrieval actually succeeded. 3. Inspect message, subtotal and action. | Cart is empty, CAD 0.00 and Continue shopping. Do not infer emptiness from an error. | Not run | |
| CART-T-04 / CART-AC-04 | F1 once prerequisites exist. 1. Developer/tester enables a reversible cart-read server error. 2. Customer opens View cart. 3. Inspect message, action and totals area. | Couldn't load your cart. Please try again.; Retry available; no confirmed empty-cart or zero-subtotal claim. Current actual readiness results are in BLK-CART-01, not an executed server-error scenario. | Blocked: BLK-CART-01 | |
| CART-T-05 / CART-AC-05 | Continue controlled setup from T-04. 1. Record saved fixture. 2. Select Retry with failure active. 3. Verify another cart read and repeated error. 4. Remove failure; select Retry again. 5. Compare displayed and saved data. | Retry reads rather than mutates. Error remains while failure is active; recovery shows original F1 values and clears the load error. No items/quantities changed. | Blocked: BLK-CART-01 | |
| CART-T-06 / CART-AC-06 | Run separately from F0 and F1. 1. Open cart. 2. Select Continue shopping. 3. Reopen cart through a fresh retrieval and compare saved contents. | Navigate to product browsing; saved contents unchanged in both variants. | Not run | |
| CART-T-07 / CART-AC-07 | Run against each implemented cart state in scope; log unavailable states separately. 1. Open/trigger the state. 2. Inspect demo pricing wording. | Demo only. Tax and shipping are not calculated. No payment is taken. Wording does not promise actual payment or delivery. | Not run | |

## Quantity validation and confirmed outcomes

| Test / criterion | Setup and procedure | Expected result | Status | Actual / evidence |
|---|---|---|---|---|
| CART-T-08 / CART-AC-08 | F1. 1. Enter 10. 2. Select Update quantity once and await confirmed success. 3. Reopen with fresh retrieval; compare saved state. | Quantity 10, line/subtotal CAD 125.00, Quantity updated successfully.; requested value is saved. | Not run | |
| CART-T-09 / CART-AC-09 | F1. 1. Enter 1. 2. Update once and await confirmed success. 3. Reopen and compare saved state. | Quantity 1, line/subtotal CAD 12.50 and success message; quantity 1 is saved. | Not run | |
| CART-T-10 / CART-AC-10 | F1 reset before each input: 0, -1, 1.5, text, blank and 11. 1. Enter input. 2. Attempt update. 3. Inspect validation. 4. Verify saved state unchanged; correct to a valid value to check correction is possible. | Enter a whole number from 1 to 10.; rejection preserves quantity 2 and CAD 25.00 totals before correction. Record each invalid variant independently. | Not run | |
| CART-T-11 / CART-AC-11 | Use the full procedure and record template in [CART-UAT-01](quantity-update-uat-case.md). F2; change mugs from 2 to 3. | Mug line CAD 37.50, mouse CAD 24.99, subtotal CAD 62.49; verify success and persistence as specified there. This row links the existing case rather than duplicating execution. | Not run | |
| CART-T-12 / CART-AC-12 | F1. Technical support configures confirmed rejection/failure before saving, not a lost response. 1. Request 3. 2. Inspect response and feedback. 3. Retrieve/verify saved data. 4. Observe whether any repeat occurs without customer choice. | Quantity 2 and CAD 25.00 remain. Update failed. Please try again. Retry is customer-controlled; no automatic update. Remove failure control after evidence capture. | Not run | |

Persistence checks support the intended saved-change outcome; review these checks with the team before baseline as noted in CART-UAT-01. Retention-reset expectations are tested separately below.

## Quantity-update recovery and conflicting actions

These procedures require implemented, reliable original-request status tracking and safe terminal-state guarantees. CART-Q-01 through CART-Q-03 remain unresolved. Do not fabricate processing or final status by interpreting a timeout or saved quantity alone. Have the technical reviewer agree controlled request states and evidence before execution. Prolonged unknown recovery is outside these defined branches and remains an open requirement.

| Test / criterion | Setup and procedure | Expected result | Status | Actual / evidence |
|---|---|---|---|---|
| CART-T-13 / CART-AC-13 | F1; original request to set quantity 3 has an unconfirmed outcome. 1. Display that state. 2. Attempt to remove the same mug line. 3. Inspect controls and request evidence. | Removal prevented; explanation that earlier update is unconfirmed; Check update status available. No remove request takes effect. | Not run | |
| CART-T-14 / CART-AC-14 | F1 with original request unresolved. 1. Record original request identity and mutation count. 2. Select Check update status. 3. Compare network/backend request records. | Status of that original request is checked; no new quantity update or removal is submitted. | Not run | |
| CART-T-15 / CART-AC-15 | F1; request quantity 3 initially unconfirmed, then technically confirmed terminal success with no further effect possible. 1. Check status. 2. Let fresh cart read succeed. 3. Inspect values and removal availability. | Quantity 3, line/subtotal CAD 37.50, Update confirmed. No repeated mutation; removal enabled after safe resolution and successful retrieval. | Not run | |
| CART-T-16 / CART-AC-16 | Same terminal-success setup as T-15; cart read then fails. 1. Check status. 2. Trigger/read controlled retrieval failure. 3. Inspect message and controls. | Update confirmed, but we couldn't refresh your cart. Removal stays unavailable; old values labelled last confirmed; Refresh cart available. | Not run | |
| CART-T-17 / CART-AC-17 | Continue T-16; remove only cart-read failure. 1. Select Refresh cart. 2. Inspect new read and displayed saved data. 3. Inspect removal control. | Current data displayed, quantity 3/CAD 37.50 for this fixture; removal enabled if line exists. No repeat of original update. | Not run | |
| CART-T-18 / CART-AC-18 | F1; original request quantity 3 becomes terminal failure before mutation; fresh read succeeds. 1. Check original status. 2. Read cart. 3. Inspect values and available actions. | Quantity 2, line/subtotal CAD 25.00, failure message; removal enabled and customer may choose update retry. No automatic repeat. | Not run | |
| CART-T-19 / CART-AC-19 | F1; technical evidence confirms original update is processing. 1. Select status check. 2. Inspect verified processing feedback. 3. Attempt another update/removal for same line. | Both changes remain unavailable; Check update status remains available. Exact processing wording needs review before text-specific assertions are baselined. | Not run | |
| CART-T-20 / CART-AC-20 | F1; unresolved original update and controlled status-check failure. 1. Check status. 2. Inspect old values, message and controls. 3. Check again while failure remains. | Outcome remains unconfirmed, not asserted processing/failed; old values last confirmed, affected changes blocked, status checking available without mutation. Repeated checking is not a complete prolonged-recovery policy. | Not run | |

## Item removal, logout and merging

| Test / criterion | Setup and procedure | Expected result | Status | Actual / evidence |
|---|---|---|---|---|
| CART-T-21 / CART-AC-21 | F2; no unresolved earlier change. 1. Remove mug line once. 2. Await confirmed success. 3. Reopen and compare saved contents. | Both mugs gone; only mouse quantity 1 remains, line/subtotal CAD 24.99 and Item removed successfully. | Not run | |
| CART-T-22 / CART-AC-22 | F1. 1. Remove mug line. 2. Await confirmed success. 3. Retrieve again. | No mug units or other items remain; Cart is empty, CAD 0.00 and Continue shopping. | Not run | |
| CART-T-23 / CART-AC-23 | F1; controlled confirmed removal rejection before mutation. 1. Remove mug line. 2. Inspect failed result. 3. Verify saved cart and whether automatic retry occurs. | Both mugs and CAD 25.00 remain; Item removal failed. Please try again.; customer decides retry. Remove failure control afterward. | Not run | |
| CART-T-24 / CART-AC-24 | F1; requires agreed successful-logout/security guarantee under CART-Q-08. 1. Log out using implemented control. 2. Verify agreed termination evidence. 3. Attempt protected cart change. 4. Sign in again and retrieve fixture; inspect expiry with technical support. | Protected change requires reauthentication; saved cart and expiry preserved. Token revocation assertions cannot be finalized until scope is decided. Do not imply local token deletion proves revocation. | Not run | |
| CART-T-25 / CART-AC-25 | F1. 1. Add one exact same product/variant from its add flow. 2. Await confirmed save. 3. Retrieve cart and verify saved lines. | One mug line, quantity 3, unit CAD 12.50, line/subtotal CAD 37.50; no duplicate product/variant row displayed. | Not run | |
| CART-T-26 / CART-AC-26 | F10. 1. Add one identical mug. 2. Inspect rejection. 3. Re-read saved cart. | Still one line quantity 10, CAD 125.00 totals; Maximum quantity of 10 reached for this product/variant. No other product quota is implied. | Not run | |
| CART-T-27 / CART-AC-27 | Two blue mugs saved; separate red variant available, with verified fixture prices. 1. Add one red mug. 2. Await success. 3. Retrieve lines. | Blue quantity 2 and red quantity 1 in distinct lines. Record prices/totals from the controlled fixture, not an invented red-variant price. | Not run | |

## Retention and expiry

Use an agreed controllable test clock or supported fixture timestamps. Do not alter the host clock or production data. Let T denote the stored last successful change and E = T plus 30 times 24 hours. Verify comparisons with technical support; capture clock/time-zone interpretation and leave in-flight expiry interactions outside these cases until resolved.

| Test / criterion | Setup and procedure | Expected result | Status | Actual / evidence |
|---|---|---|---|---|
| CART-T-28 / CART-AC-28 | F1 with retention elapsed; no in-flight changes. 1. Retrieve cart at agreed post-expiry test time. 2. Inspect contents and message. | No expired items returned/displayed; expiry explanation, CAD 0.00 and Continue shopping. Physical cleanup timing need not match logical expiry. | Not run | |
| CART-T-29 / CART-AC-29 | F1; last successful change 20 elapsed days earlier. 1. Record E. 2. Sign in and retrieve. 3. Compare saved contents and E. | Active fixture shown; sign-in/viewing do not change E. Ten elapsed days remain absent another successful change. | Not run | |
| CART-T-32 / CART-AC-32 | F1 at day 20; successful-logout guarantee agreed. 1. Record E. 2. Log out successfully. 3. Verify retained saved items and E using authorized method. | Items retained; E unchanged, ten days remain. No restart from logout. | Not run | |
| CART-T-33 / CART-AC-33 | F1 last changed 20 days ago. 1. Record old E. 2. Successfully set quantity 3 at controlled time T2. 3. Inspect recorded retention reference and new expiry. | New expiry T2 plus 30 times 24 hours, replacing the old E. Define authoritative successful-change timestamp through technical review. | Not run | |
| CART-T-34 / CART-AC-34 | F1 at day 20; controlled confirmed save rejection. 1. Record E. 2. Request quantity 3 and confirm failure. 3. Inspect contents and E. | Quantity 2 retained and E unchanged; ten days remain. Remove failure control afterward. | Not run | |
| CART-T-35 / CART-AC-35 | F1 at E minus one second. 1. Retrieve at that controlled instant. 2. Inspect active items and E. | Cart remains active with fixture values; retrieval does not reset expiry. | Not run | |
| CART-T-36 / CART-AC-36 | Reset independent F1 variants at exactly E and at E plus one second. 1. Retrieve each. 2. Compare contents/message/subtotal/actions. | Both are expired: no active expired items, explanation, CAD 0.00 and Continue shopping. Record each boundary variant separately. | Not run | |

## Price changes

| Test / criterion | Setup and procedure | Expected result | Status | Actual / evidence |
|---|---|---|---|---|
| CART-T-30 / CART-AC-30 | F1 previously displayed at CAD 12.50; technical setup changes current mug price to CAD 14.00. 1. Refresh successfully. 2. Inspect affected line notice, prices and totals. | Old CAD 12.50/new CAD 14.00 explicit in text; unit CAD 14.00, quantity 2, line/subtotal CAD 28.00. Meaning does not depend on colour. | Not run | |
| CART-T-31 / CART-AC-31 | F1 last confirmed price CAD 12.50; controlled cart refresh failure. 1. Refresh. 2. Inspect message and retained price labels. 3. Inspect available action. | No new price claimed; retained prices/totals labelled last confirmed; We couldn't refresh your cart. Please try again.; Refresh cart. This state is not fully designed yet. | Not run | |
| CART-T-37 / CART-AC-37 | Only two mugs previously displayed at CAD 14.00; current price changes to CAD 12.50. 1. Refresh successfully. 2. Inspect affected-line notice and recalculate totals. | Old CAD 14.00/new CAD 12.50 in text; unit CAD 12.50, line/subtotal CAD 25.00. Meaning does not depend on colour. | Not run | |

Restore controlled catalog prices after price cases. Do not reuse changed fixtures in other cases without a reset.

## Review gaps, additional coverage and next step

- Keep logout guarantees, prolonged recovery, session-expiry behaviour and concurrency open under CART-Q-01 through CART-Q-08 as applicable; this pack does not decide them.
- Add separately recorded successful-addition/removal retention-reset cases from DEC-08 during review. CART-T-33 currently covers quantity change only.
- Review additional coverage for multiple product lines, differing variants and price changes, customer ownership, keyboard/focus/status announcements and unexpected responses. This pack covers the existing 37 criteria, not every necessary release test.
- Request identity, mutation counts, persistence and expiry require technical evidence beyond customer screenshots. Agree safe access and evidence limitations before execution.
- Several controls/screens are not implemented and some wireframe states remain missing; local prototype checks do not establish application readiness.
- Every blank result above is intentional. No simulated defect or role response is execution evidence. The two existing Blocked records are actual readiness findings, not failed cart-error tests.

Next: review the pack with the appropriate roles, agree missing expectations and test-support methods, prioritize an implementation slice and environment setup, then execute only cases whose prerequisites are verified. Record real results and defects/retests as they occur.
