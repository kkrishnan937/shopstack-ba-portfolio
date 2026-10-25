# First-increment cart requirements

**Version:** 0.1  
**Date:** 25 October 2026  
**Status:** Draft consolidated from simulated requirements workshops; review pending  
**Author:** Kailas Krishnan, portfolio author practising the BA role

## Scope and evidence

Consolidates the cart-review and quantity-update criteria practised in discussion. These describe intended behaviour, not implemented features, executed tests, or independent stakeholder approval. Request-status tracking and safe resolution are proposed capabilities whose feasibility has not been verified. Simulated estimates and release dates are not actual project forecasts.

Sources: [gap register](../process-analysis/gap-register.md), [decision record](../process-analysis/prioritization-and-decisions.md), [future-state process](../process-analysis/future-state-cart-process.md), and [recovery workshop](../discovery/cart-recovery-workshop-2026-10-25.md). Earlier process documents require reconciliation with these later discussions.

IDs in this document form the portfolio's working story namespace. The earlier starter material under the application repository's `docs/ba-portfolio` used different story numbering and is not this requirements baseline.

## Requirement register

| ID | Requirement | Source | Status |
|---|---|---|---|
| CART-FR-01 | A signed-in customer can review their saved cart, prices, quantities and subtotal, and return to browsing without changing it. | GAP-02; US-01 below | Draft criteria prepared |
| CART-FR-02 | A signed-in customer can request valid quantity changes, with confirmed outcomes and accurate totals. | GAP-03; US-02 below | Draft criteria prepared; recovery gaps open |
| CART-FR-03 | A customer can remove an entire cart line and receive an accurate resulting cart state. | GAP-03 | Separate removal story and full criteria pending |
| CART-FR-04 | A customer can log out while retaining the saved cart under its retention rule. | DEC-06 | Story and criteria pending |
| CART-FR-05 | Identical product/variant additions merge, subject to the combined quantity limit. | DEC-03, DEC-04 | Detailed criteria pending |
| CART-FR-06 | Saved cart retention follows the 30-day inactivity rule. | DEC-02 | Detailed criteria pending |
| CART-FR-07 | Current catalog prices are reflected with explicit notice when a cart item's price changes. | Workshop proposal | Policy details and criteria require review |

## Working business rules

| ID | Rule | Basis |
|---|---|---|
| CART-BR-01 | Quantity is a whole number from 1 to 10 per product/variant. The limit includes merged additions. | DEC-04 |
| CART-BR-02 | Invalid input does not change saved quantities, line totals or subtotal. Zero is not a removal action. | Process rules; simulated refinement |
| CART-BR-03 | Line total equals quantity multiplied by unit price; subtotal equals the sum of line totals. Display CAD with two decimal places. | DEC-05 |
| CART-BR-04 | Show success only after the requested change is confirmed. An absent response or failed status check does not establish failure or continued processing. | Recovery workshop and refinement |
| CART-BR-05 | While an item's earlier update is processing or unconfirmed, prevent further quantity updates and removal of that item. Status checks do not repeat a mutation. | Simulated recovery decision; technical review pending |
| CART-BR-06 | Re-enable removal after the original request is resolved and can no longer alter the cart, and fresh saved-cart retrieval succeeds with the item present. | Simulated refinement |
| CART-BR-07 | No stock checks or reservation are included. The quantity limit does not guarantee availability. | DEC-07 |
| CART-BR-08 | Retain the account cart for 30 days after its last successful addition, update or removal. Login expiry, logout, viewing and refreshing do not extend retention. | DEC-02, DEC-06 |

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
| CART-AC-07 | When the cart is displayed | Show "Demo only. Tax and shipping are not calculated. No payment is taken." |

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

## Open requirements and review gaps

| ID | Gap / required decision | Proposed review roles |
|---|---|---|
| CART-Q-01 | Prolonged unknown outcomes need a safe recovery policy, escalation path and conditions for restoring editing. Repeated checking is not a complete recovery solution; a timeout alone does not prove the earlier request has stopped. | Product owner, technical lead, tester |
| CART-Q-02 | Validate request-status tracking and terminal-state guarantees. A retrieved quantity alone cannot establish the final outcome of an original request that may still be processing. | Developer / technical lead |
| CART-Q-03 | Define behaviour when status confirms failure but cart retrieval fails; also review overlapping actions on other items and cart changes from other sessions. | Product owner, developer, tester |
| CART-Q-04 | Complete session-expiry criteria, including safe handling of an update accepted before expiry. Do not assume expiry cancels an in-flight request. | Developer, product owner, tester |
| CART-Q-05 | Review accessibility, focus, status announcements, messages, and how blocked actions are explained. | UX/content, tester, customer representative |
| CART-Q-06 | Complete removal, logout, merging, retention boundary and price-change stories. Price notice should use text rather than colour alone; details need review. | BA, product owner, developer, tester |
| CART-Q-07 | Reconcile process diagrams and written process with the later rules, and trace criteria to tests before execution. | BA with delivery review |

## Readiness and next step

This is a review draft, not a release baseline. The full update story is not ready for release while prolonged recovery is unresolved. Independent validation and confirmed-outcome work may progress if the delivery team agrees the split; testing requires implemented behaviour. No criteria in this document have recorded execution results.

Next: review these criteria for consistency, complete the removal story, and continue the remaining cart criteria before returning to the stakeholder plan review, as requested by the portfolio author.
