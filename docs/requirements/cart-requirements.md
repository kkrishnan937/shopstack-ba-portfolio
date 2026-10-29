# First-increment cart requirements

**Version:** 0.4
**Date:** 28 October 2026
**Status:** Draft consolidated from simulated requirements workshops; review pending  
**My role:** I acted as the BA, with AI-assisted documentation.

## Scope and evidence

**Actual execution update:** The [local cart-viewing run](../testing/cart-view-executed-2026-10-28.md) now implements and verifies the read-only path. CART-AC-01 through CART-AC-07, CART-AC-28 and CART-AC-29 have corresponding local Pass evidence. Other criteria remain unexecuted. This does not approve the full baseline or implement the mutation/recovery scope described below.

**Latest change:** [CR-CART-01](cart-readiness-change-and-handoff.md) records the author's dedicated-page, server amount, token-expiry reconciliation, expiry-flag, logout invalidation and release-gate decisions. It also adds tax/shipping calculation to wider checkout scope, with calculation inputs still open. Existing 37 criteria need expansion for these new constraints. Earlier proposals are superseded where they conflict; this is not an independently approved or implemented baseline.

Consolidates the cart-review and quantity-update criteria practised in discussion. These describe intended behaviour, not implemented features, executed tests, or independent stakeholder approval. Request-status tracking and safe resolution are proposed capabilities whose feasibility has not been verified. Simulated estimates and release dates are not actual project forecasts.

Sources: [gap register](../process-analysis/gap-register.md), [decision record](../process-analysis/prioritization-and-decisions.md), [future-state process](../process-analysis/future-state-cart-process.md), and [recovery workshop](../discovery/cart-recovery-workshop-2026-10-25.md). Earlier process documents require reconciliation with these later discussions.

IDs in this document form the portfolio's working story namespace. The earlier starter material under the application repository's `docs/ba-portfolio` used different story numbering and is not this requirements baseline.

## Requirement register

| ID | Requirement | Source | Status |
|---|---|---|---|
| CART-FR-01 | A signed-in customer can review their saved cart, prices, quantities and subtotal, and return to browsing without changing it. | GAP-02; US-01 below | Draft criteria prepared |
| CART-FR-02 | A signed-in customer can request valid quantity changes, with confirmed outcomes and accurate totals. | GAP-03; US-02 below | Draft criteria prepared; recovery gaps open |
| CART-FR-03 | A customer can remove an entire cart line and receive an accurate resulting cart state. | GAP-03 | Main and confirmed-failure criteria drafted; unknown-outcome recovery open |
| CART-FR-04 | A customer can log out, invalidating the token while retaining the saved cart under its retention rule. | DEC-06; CR-CART-01 | Required release blocker; design, failure and verification criteria pending |
| CART-FR-05 | Identical product/variant additions merge, subject to the combined quantity limit. | DEC-03, DEC-04 | Main and exception criteria drafted; review gaps open |
| CART-FR-06 | Saved cart retention follows the 30-day inactivity rule. | DEC-02 | Main and exception criteria drafted; review gaps open |
| CART-FR-07 | Current catalog prices are reflected with explicit notice when a cart item's price changes. | DEC-09 | Policy recorded for case study; implementation and independent review pending |

## Working business rules

| ID | Rule | Basis |
|---|---|---|
| CART-BR-01 | Quantity is a whole number from 1 to 10 per product/variant. The limit includes merged additions. | DEC-04 |
| CART-BR-02 | Invalid input does not change saved quantities, line totals or subtotal. Zero is not a removal action. | Process rules; simulated refinement |
| CART-BR-03 | Backend calculates amounts in integer cents; client formats authoritative values as CAD with two decimals. Line total is quantity times unit price; subtotal sums line totals. No tax/shipping total in cart. | DEC-05 amended by CR-CART-01 |
| CART-BR-04 | Show success only after the requested change is confirmed. An absent response or failed status check does not establish failure or continued processing. | Recovery workshop and refinement |
| CART-BR-05 | While an item's earlier update is processing or unconfirmed, prevent further quantity updates and removal of that item. Status checks do not repeat a mutation. | Simulated recovery decision; technical review pending |
| CART-BR-06 | Re-enable removal after the original request is resolved and can no longer alter the cart, and fresh saved-cart retrieval succeeds with the item present. | Simulated refinement |
| CART-BR-07 | No stock checks or reservation are included. The quantity limit does not guarantee availability. | DEC-07 |
| CART-BR-08 | Retain the account cart for 30 days after its last successful addition, update or removal. Login expiry, logout, viewing and refreshing do not extend retention. | DEC-02, DEC-06 |
| CART-BR-09 | Token lapse requires sign-in before protected changes. Backend reconciles pre-expiry updates using idempotency keys and cart versions; stale versions return conflict and require refetch before safe retry. | CR-CART-01; contract details pending |
| CART-BR-10 | Cart-record expiry flag survives repeat visits and failed additions; clear only on successful addition. Dismiss hides the explanation for the current view only. Session expiry does not trigger it. Later removal does not restore old expiry reason. | CR-CART-01 |
| CART-BR-11 | No cart mutations ship until session-expiry reconciliation, logout token invalidation and retention response contract close. Other release conditions remain applicable. | CR-CART-01 |

## US-01: Review my cart

As a signed-in customer, I want to review my cart so I can verify my selections before making changes or submitting a demo order.

Each criterion assumes access to the customer's own cart.

| ID | Given / When | Then |
|---|---|---|
| CART-AC-01 | Given a signed-in customer, when their non-empty saved cart loads successfully | Display each product's name, unit price, quantity and line total, plus cart subtotal. Show money in CAD with two decimal places. |
| CART-AC-02 | Given 2 mugs at CAD 12.50 each and 1 mouse at CAD 24.99, when the cart loads | Show mug line total CAD 25.00, mouse line total CAD 24.99, and subtotal CAD 49.99. |
| CART-AC-03 | When successful retrieval confirms no saved items | Show "Cart is empty", subtotal CAD 0.00 and Continue shopping. |
| CART-AC-04 | When cart retrieval fails | Show "Couldn't load your cart. Please try again." and Retry. Do not represent the cart as confirmed empty or its subtotal as confirmed zero. |
| CART-AC-05 | Given a cart-loading failure, when the customer selects Retry | Retrieve the current saved cart again without adding, updating or removing items. |
| CART-AC-06 | Given an empty or non-empty cart, when the customer selects Continue shopping | Return to product browsing on the home page without changing saved items. |
| CART-AC-07 | When the cart is displayed | Show "Cart subtotal only. Tax and shipping are calculated at demo checkout. No payment is taken." This identifies the wider checkout policy, not existing implementation. |

## US-02: Update cart quantity

As a signed-in customer, I want to change a product's quantity so I can correct my cart before submitting a demo order.

Unless specified otherwise, examples contain only 2 mugs at CAD 12.50 each, and assume no concurrent price or cart changes. Boundary criteria test a changed quantity, not saving an unchanged value.

| ID | Given / When | Then |
|---|---|---|
| CART-AC-08 | Given the example cart, when quantity is changed to 10 and saving succeeds | Show quantity 10, line total CAD 125.00, subtotal CAD 125.00 and "Quantity updated successfully." |
| CART-AC-09 | Given the example cart, when quantity is changed to 1 and saving succeeds | Show quantity 1, line total CAD 12.50, subtotal CAD 12.50 and "Quantity updated successfully." |
| CART-AC-10 | Given a saved quantity of 2, when the customer attempts an update with 0, -1, 1.5, text, blank input, or 11 | Reject the input, show "Enter a whole number from 1 to 10.", allow correction, and leave saved quantity, line total and subtotal unchanged. Verify each input separately. |
| CART-AC-11 | Given 2 mugs at CAD 12.50 and 1 mouse at CAD 24.99, when mug quantity is changed to 3 and saving succeeds | Show mug quantity 3, mug line total CAD 37.50, subtotal CAD 62.49 and "Quantity updated successfully." Unit prices remain unchanged in this scenario. |
| CART-AC-12 | Given the example cart, when quantity 3 is requested and saving is confirmed failed | Show confirmed quantity 2, line total CAD 25.00, subtotal CAD 25.00 and "Update failed. Please try again." Let the customer choose whether to retry; do not retry automatically. |
| CART-AC-13 | Given an item's earlier quantity update has an unconfirmed outcome, when the customer attempts to remove that same item | Prevent removal, explain that the earlier update has not been confirmed, and offer Check update status. Candidate message: "We haven't confirmed your earlier quantity update yet. Removal is temporarily unavailable. Select 'Check update status' to check again." |
| CART-AC-14 | Given an earlier quantity update remains unconfirmed, when the customer selects Check update status | Check the original request's status without submitting another quantity update or removal. |
| CART-AC-15 | Given the example cart and a requested quantity of 3, when the status check confirms terminal success and fresh cart retrieval confirms quantity 3 | Show quantity 3, line total CAD 37.50, subtotal CAD 37.50 and "Update confirmed." Do not repeat the update. Enable removal only after the original request can no longer alter the cart and retrieval has succeeded. |
| CART-AC-16 | Given the original update is confirmed successful, when fresh cart retrieval fails | Explain "Update confirmed, but we couldn't refresh your cart." Keep removal unavailable and offer Refresh cart. Any previously displayed values remain labelled last confirmed rather than current. |
| CART-AC-17 | Given the original update is terminally successful and removal stayed unavailable because retrieval failed, when Refresh cart successfully retrieves the affected item | Display current saved products, quantities, unit prices, line totals and subtotal, and enable removal for that item. Refresh must not repeat the original update. |
| CART-AC-18 | Given the example cart and requested quantity 3, when status checking confirms terminal failure and fresh retrieval succeeds with quantity 2 | Show quantity 2, line total CAD 25.00, subtotal CAD 25.00 and "Update failed. Please try again." Enable removal and let the customer choose whether to retry the update; do not retry automatically. |
| CART-AC-19 | Given an unresolved quantity update, when a status check confirms processing | Explain the verified processing state, keep further quantity updates and removal unavailable for that item, and offer Check update status. Exact processing message requires review. |
| CART-AC-20 | Given an unresolved quantity update, when its status check fails | Explain that the outcome remains unconfirmed, keep further quantity updates and removal unavailable for that item, and offer Check update status again. Do not claim "Still processing" solely because the check failed. Previously displayed values must be labelled last confirmed. |

## US-03: Remove a cart item

As a signed-in customer, I want to remove an unwanted product so I can correct my cart.

Removal deletes the entire product line, not one unit. These cases assume no unresolved earlier mutation for that item; CART-AC-13 governs that restriction.

| ID | Given / When | Then |
|---|---|---|
| CART-AC-21 | Given 2 mugs at CAD 12.50 each and 1 mouse at CAD 24.99, when the mug line is removed successfully | Display only 1 mouse, line total CAD 24.99, subtotal CAD 24.99, and "Item removed successfully." |
| CART-AC-22 | Given the cart contains only 2 mugs, when their entire line is removed successfully | Display "Cart is empty", subtotal CAD 0.00 and Continue shopping. |
| CART-AC-23 | Given only 2 mugs at CAD 12.50 each, when removal is confirmed failed | Keep both mugs, line total and subtotal CAD 25.00, and display "Item removal failed. Please try again." Let the customer choose whether to retry; do not retry automatically. |

## US-04: Log out

As a signed-in customer, I want to log out so I can end my session.

| ID | Given / When | Then |
|---|---|---|
| CART-AC-24 | Given a signed-in customer with a saved cart, when the customer selects Logout and logout succeeds | End the signed-in session, retain saved items under the existing 30-day retention rule, and require sign-in before protected cart changes. Logout does not reset the retention clock. |

## US-05: Merge identical product additions

As a signed-in customer, I want repeated additions of the same product and variant combined so I can review their total quantity clearly.

| ID | Given / When | Then |
|---|---|---|
| CART-AC-25 | Given 2 mugs of the same product/variant at CAD 12.50 each, when 1 identical mug is added and saving succeeds | Display one mug line, quantity 3, unit price CAD 12.50 and line total CAD 37.50. Product/variant identity, not matching price alone, determines merging. |
| CART-AC-26 | Given 10 identical mugs, when another identical mug is added | Reject the addition, preserve saved quantity 10 and totals, and explain "Maximum quantity of 10 reached for this product/variant." The rule does not limit all products combined to 10 units. |
| CART-AC-27 | Given 2 blue mugs, when 1 red mug is added successfully as a different variant | Display two separate product/variant lines: blue mugs quantity 2 and red mug quantity 1. |

## US-06: Retain and expire the saved cart

As a customer, I want my cart retained for the agreed period so I can return to my selections later.

| ID | Given / When | Then |
|---|---|---|
| CART-AC-28 | Given the cart's 30-day retention period since its last successful change has elapsed, when the customer next opens the cart and retrieval succeeds | Return no expired saved items, display "Your saved cart expired after 30 days without changes", subtotal CAD 0.00 and Continue shopping. Physical cleanup timing is a design matter; expired contents must not be presented as an active cart. |
| CART-AC-29 | Given the last successful cart change was 20 days ago, when the customer signs in and successfully retrieves the cart | Display the saved items subject to current pricing rules. Sign-in and viewing do not reset retention; absent further successful changes, expiry remains 30 days after the last successful change. |

## US-07: Handle product price changes

As a customer, I want to see current prices and be informed of changes so I can review the cost of my selections.

The current-price policy was confirmed within the simulated refinement under DEC-09. It applies to increases and decreases; this is a case-study decision, not independent approval or implemented behaviour.

| ID | Given / When | Then |
|---|---|---|
| CART-AC-30 | Given only 2 mugs previously displayed at CAD 12.50 each, when refreshing retrieves the current unit price CAD 14.00 | Display unit price CAD 14.00, line total CAD 28.00 and subtotal CAD 28.00, with text "Price changed from CAD 12.50 to CAD 14.00." Colour may supplement the notice but cannot be its only indication. |
| CART-AC-31 | Given the last confirmed mug price CAD 12.50, when refreshing the cart fails | Do not claim a new price is confirmed. Explain "We couldn't refresh your cart. Please try again." and offer Refresh cart. If previous prices or totals remain visible, label them last confirmed rather than current. |

## Additional retention and price criteria from refinement

These cases assume no unresolved in-flight cart changes. Time T denotes the recorded last successful cart change; exact expiry is T plus 30 times 24 hours.

| ID | Given / When | Then |
|---|---|---|
| CART-AC-32 | Given the last successful cart change was 20 days ago, when logout succeeds | Retain saved items with the original expiry unchanged, leaving 10 days if no further successful changes occur. This criterion does not settle the technical guarantee of successful logout. |
| CART-AC-33 | Given the last successful cart change was 20 days ago, when a quantity change succeeds at time T | Set expiry to T plus 30 times 24 hours, unless another successful change resets it. |
| CART-AC-34 | Given the last successful cart change was 20 days ago, when a quantity update is confirmed failed | Preserve the original expiry, leaving 10 days if no further successful changes occur. |
| CART-AC-35 | Given a non-empty cart last changed successfully at T, when retrieval succeeds one second before T plus 30 times 24 hours | Treat the cart as active and display saved items subject to current pricing rules; retrieval does not reset expiry. |
| CART-AC-36 | Given a non-empty cart last changed successfully at T, when retrieval succeeds exactly at T plus 30 times 24 hours or afterward | Treat the cart as expired, exclude expired saved items, explain expiry, and display subtotal CAD 0.00 and Continue shopping. Test the exact instant and an instant after it separately. |
| CART-AC-37 | Given only 2 mugs previously displayed at CAD 14.00 each, when refresh retrieves the current price CAD 12.50 | Display unit price CAD 12.50, line total CAD 25.00, subtotal CAD 25.00 and text "Price changed from CAD 14.00 to CAD 12.50." |

## Open requirements and review gaps

| ID | Gap / required decision | Proposed review roles |
|---|---|---|
| CART-Q-01 | Prolonged unknown outcomes need a safe recovery policy, escalation path and conditions for restoring editing. Repeated checking is not a complete recovery solution; a timeout alone does not prove the earlier request has stopped. | Product owner, technical lead, tester |
| CART-Q-02 | Validate request-status tracking and terminal-state guarantees. A retrieved quantity alone cannot establish the final outcome of an original request that may still be processing. | Developer / technical lead |
| CART-Q-03 | Define behaviour when status confirms failure but cart retrieval fails; also review overlapping actions on other items and cart changes from other sessions. | Product owner, developer, tester |
| CART-Q-04 | Complete session-expiry criteria, including safe handling of an update accepted before expiry. Do not assume expiry cancels an in-flight request. | Developer, product owner, tester |
| CART-Q-05 | Review accessibility, focus, status announcements, messages, and how blocked actions are explained. | UX/content, tester, customer representative |
| CART-Q-06 | Review US-03 through US-07 criteria; complete removal unknown-outcome recovery and logout failure. Define retention-message behaviour and expiry interactions with in-flight requests. DEC-08 and DEC-09 now clarify elapsed-time boundaries and basic current-price policy. Add explicit successful-addition/removal retention-reset cases in test planning. | BA, product owner, developer, tester |
| CART-Q-08 | Token invalidation is required as a release blocker under CR-CART-01. Define scope, failure handling, active-request boundaries and verification; current code has no implemented logout/revocation. No verified estimate or actual assignee. | Backend/Security, product owner, tester |
| CART-Q-07 | Reconcile process diagrams and written process with the later rules, and trace criteria to tests before execution. | BA with delivery review |

### Updated disposition under CR-CART-01

CART-Q-04 now needs criteria/contract expansion for required token-lapse, idempotency and cart-version conflict handling. CART-Q-06 now has a decided message-lifetime/dismissal rule; storage/API details, in-flight interactions and criteria remain open. CART-Q-08 no longer asks whether invalidation belongs in scope: it is required as a release blocker, with technical design, failure behaviour and verification open. Simulated owners/targets are Backend/Security in Sprint 1 for invalidation, Backend Lead in Sprint 1 for retention contract, and Product/UX in Sprint 2 for prolonged recovery. No actual staffing, dates or estimates are established.

Additional review: define integer-cent amount fields and authoritative backend calculations; define checkout tax/shipping rates, bases and exact once-per-order half-up rounding sequence. No regulatory assumptions or checkout implementation are supplied.

## Readiness and next step

This is a review draft, not a release baseline. The full update story is not ready for release while prolonged recovery is unresolved. Independent validation and confirmed-outcome work may progress if the delivery team agrees the split; testing requires implemented behaviour. No criteria in this document have recorded execution results.

Next: review actual read-only execution evidence and remaining contract/acceptance gaps before extending the delivered path. Version 0.4 retains 37 criterion IDs and does not exhaust new constraints; nine have local test-family Pass evidence, while 28 remain unexecuted. No complete-release approval is implied.
