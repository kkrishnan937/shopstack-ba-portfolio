# ShopStack: Future-State Cart Process

**Prepared by:** Kailas Krishnan  
**Date:** 25 October 2026  
**Version:** 0.3
**Status:** Proposed process: draft for review

## Purpose and boundaries

Define how existing signed-in customers will review and manage their cart in the first increment. The process addresses [GAP-02 and GAP-03](gap-register.md), following [DEC-01](prioritization-and-decisions.md).

The customer is already signed in. Registration and demo order submission remain part of the wider release rather than this increment. Logout is included in the first increment under DEC-06, but its success guarantees, token invalidation and failure behaviour remain unresolved. This draft describes intended behaviour, not implemented functionality or completed acceptance testing.

This revision reconciles the written process with [requirements v0.3](../requirements/cart-requirements.md) and DEC-02 through DEC-09 in the [decision record](prioritization-and-decisions.md). Decisions and reviews are part of a simulated case study, not independent approval. Earlier diagram exports have not yet been reconciled; see the diagram change list below.

## Proposed entry and exit

- Entry: A signed-in customer requests to view their cart.
- Exit: The customer leaves the cart to continue shopping or closes the cart view. Closing a side panel applies only if that design is selected.
- Customers may review the cart and repeat quantity updates or removals while remaining in the cart view.
- A View cart button and a side panel on the catalog page are candidate design choices, pending wireframe review.

## 1. Open and load the cart

1. Customer requests to view the cart.
2. System attempts to retrieve the customer's saved cart, applying the retention rule in section 5 and current-price rule in section 6.
3. Decision: **Did the cart load successfully?**
   - No: Display “Couldn’t load your cart. Please try again.” Do not describe the cart as empty. A retry requests the cart again, returning to step 2.
   - Yes: Continue to step 4.
4. Decision: **Is the cart empty?**
   - Yes: Display “Cart is empty,” subtotal **CAD 0.00**, and a **Continue shopping** action that returns the customer to product browsing.
   - No: Display product names, quantities, unit prices, line totals, and the cart subtotal in CAD. Provide Update quantity, Remove item, and Continue shopping actions.

5. From a non-empty cart, the customer may select Continue shopping without updating quantities or removing items. Return to product browsing with the saved cart contents unchanged.

The contents are unknown when loading fails. An empty-cart message is appropriate only after successful retrieval confirms no items.

Display "Demo only. Tax and shipping are not calculated. No payment is taken." alongside item-price subtotals. Retrieval and browsing do not restart cart retention.

## 2. Update quantity

1. Customer enters a new quantity for an existing cart line.
2. Decision: **Is the quantity a whole number from 1 to 10?**
   - No: Display "Enter a whole number from 1 to 10." Reject blank input, text, decimals, zero, negative numbers and values above 10. Do not change saved quantities or totals. Allow correction and another attempt.
   - Yes: Attempt to save the requested quantity.
3. Decision: **Was the quantity update saved successfully?**
   - Yes: Display the confirmed saved quantity, recalculate that product's line total and the cart subtotal, and display "Quantity updated successfully." Reset retention from the successful change. Return to cart review.
   - Confirmed failure: Display “Update failed. Please try again.” Restore the last confirmed saved quantity, line total, and subtotal; allow another attempt.
   - Outcome unknown: Do not claim success or failure or assert that previous values are current. Follow section 4. A missing response is not a confirmed failure.

Quantity-only calculation examples assume no concurrent price change; a successful refresh applies the current-price rule in section 6. Quantity zero is rejected; removing the product uses the separate Remove action. A confirmed failed attempt does not reset retention. Authentication expiry and concurrent changes remain open review items.

## 3. Remove an item

1. Customer selects Remove for a cart line. Prevent removal if that item's earlier quantity update is processing or unconfirmed, explain the restriction, and offer Check update status as described in section 4.
2. System attempts to remove that line from the saved cart.
3. Decision: **Was the item removed successfully?**
   - Confirmed failure: Keep the item, quantity, and subtotal unchanged. Display “Item removal failed. Please try again.” Allow another attempt.
   - Outcome unknown: Do not claim that removal succeeded or failed or repeat removal automatically. Present verified saved state where available without treating retrieval alone as proof that an earlier request has stopped. Detailed removal-request tracking and prolonged recovery remain open under CART-Q-01 through CART-Q-03 and CART-Q-06.
   - Yes: Remove the entire line from the displayed cart, recalculate the subtotal, and display "Item removed successfully." Record the successful change for retention purposes. Continue to step 4.
4. Decision: **Is the cart empty?**
   - No: Show the remaining items and recalculated subtotal. Return to cart review.
   - Yes: Show “Cart is empty,” subtotal **CAD 0.00**, and Continue shopping.

## 4. Recover an unresolved quantity update

The following flow depends on proposed request-status tracking and safe terminal-state guarantees. Neither is verified in the current application. Requirements CART-AC-13 through CART-AC-20 define the draft expectations.

1. While an item's update is confirmed processing or has an unknown outcome, prevent another quantity update and removal for that same item. This is not an agreed lock on the entire cart.
2. Offer Check update status. It checks the original request without submitting another update or removal.
3. If processing is confirmed, explain that state and keep the affected controls unavailable.
4. If the status check fails, explain that the outcome remains unconfirmed. Do not infer processing or failure. Label any previously displayed values last confirmed and keep Check update status available.
5. If terminal success is confirmed and the request can no longer alter the cart, retrieve the saved cart. On success, display its current values and "Update confirmed"; enable removal for the affected item if it is present. Do not repeat the update.
6. If terminal failure is confirmed, retrieve the saved cart. On successful retrieval, show confirmed values and "Update failed. Please try again." Enable removal and let the customer choose whether to retry.
7. If terminal success is confirmed but cart retrieval fails, show "Update confirmed, but we couldn't refresh your cart." Keep removal unavailable, label old values last confirmed and offer Refresh cart. Successful refresh displays the saved state and enables removal for the affected item if present.

Repeated checking is not a complete prolonged-recovery policy. Safe resolution/escalation, the failure-confirmed/retrieval-failed branch, and interactions with other sessions remain unresolved. A timeout alone must not unlock editing on the assumption that the original request has stopped.

## 5. Merge products and apply retention

- Merge additions of the same product and variant into one line. Different variants remain separate; matching price alone does not identify a product.
- Enforce the combined maximum of 10 units per product/variant. Reject an addition above that limit, preserve saved values and explain "Maximum quantity of 10 reached for this product/variant."
- Retain the cart for 30 times 24 hours after the last successful addition, quantity update or removal. A new successful change restarts that period.
- Viewing, refreshing, sign-in, logout and confirmed failed changes do not reset expiry.
- Before the expiry instant the cart is active. At that instant and afterward it is expired. On successful retrieval, do not display expired saved items; explain "Your saved cart expired after 30 days without changes", show CAD 0.00 and Continue shopping.
- Cleanup timing is a technical design matter. Interactions between expiry and unresolved requests still require review.

## 6. Refresh prices and end the signed-in session

On successful refresh, use current prices for both increases and decreases. Recalculate line totals and subtotal; show a text notice identifying the old and new unit prices. Colour alone is insufficient. If refresh fails, do not claim new prices are confirmed; offer Refresh cart and label retained values last confirmed.

On successful logout, retain cart contents under their existing expiry and require sign-in before protected cart changes. Successful logout's security guarantee is not yet agreed: current code issues 24-hour JWTs and has no logout/revocation implementation. Clearing browser login state does not revoke a copied token. Token invalidation remains a proposal pending technical investigation and business scope review, not an agreed solution. Do not invent success/failure messages until that guarantee is settled.

## Proposed business rules for review

| ID | Rule |
|---|---|
| BR-CART-01 | Quantity is a whole number from 1 to 10 per product/variant, including merged additions. |
| BR-CART-02 | Removing a product removes its entire cart line; zero is not an alternative removal action. |
| BR-CART-03 | Product line total equals quantity multiplied by unit price. Cart subtotal equals the sum of product line totals. |
| BR-CART-04 | Display currency explicitly as CAD and monetary values with two decimal places. |
| BR-CART-05 | Show success only after the requested change has been confirmed successful. |
| BR-CART-06 | An invalid quantity must not change saved quantities or totals. |
| BR-CART-07 | Cart retrieval failure must not be represented as an empty cart. |
| BR-CART-08 | Identical product/variant additions merge; different variants remain separate. |
| BR-CART-09 | Retention follows the elapsed-time rule and exact expiry boundary in section 5. |
| BR-CART-10 | Refresh applies current prices with explicit text notice for increases and decreases. |
| BR-CART-11 | Stock checks and inventory reservation are excluded; the quantity limit does not guarantee availability. |
| BR-CART-12 | Block conflicting changes to an item with an unresolved update; status checking must not repeat a mutation. |

## Worked calculation

With mugs priced at CAD 12.50 each and one mouse at CAD 24.99:

- Two mugs: line total CAD 25.00; cart subtotal CAD 49.99.
- Change mugs to three: unit price remains CAD 12.50; mug line total becomes CAD 37.50; cart subtotal becomes CAD 62.49.
- Remove the mug line: only the mouse remains; subtotal becomes CAD 24.99.
- Remove the mouse: cart is empty; subtotal becomes CAD 0.00.

These are item-price subtotals. Under DEC-05 the demo does not calculate tax or shipping and takes no payment; no real-world tax-compliance claim is made.

## Open questions and review needs

| ID | Question / review need | Status |
|---|---|---|
| FS-Q-01 | Demo pricing boundary | Resolved in simulated scope under DEC-05: item-price subtotals; no tax/shipping calculation or payment |
| FS-Q-02 | Reliable request status, safe completion, prolonged recovery, and removal-specific recovery | Partially defined in section 4; CART-Q-01 through CART-Q-03 and CART-Q-06 remain open |
| FS-Q-03 | Confirm the cart entry control and whether a side panel or another layout best supports review and editing. | Proposed design; wireframe review pending |
| FS-Q-04 | Logout scope and guarantee | Inclusion in first increment resolved under DEC-06; token invalidation and failure behaviour remain open under CART-Q-08 |
| FS-Q-05 | Define behaviour when authentication expires while viewing or changing the cart. | Open; further scenario discovery required |
| FS-Q-06 | Quantity, inventory, merging, prices and retention | Core rules recorded under DEC-02 through DEC-04 and DEC-07 through DEC-09; concurrency, expiry interactions and remaining cases need review |

## Walkthrough finding: continue shopping from a non-empty cart

During the process walkthrough, the non-empty cart had no explicit route to product browsing without an update or removal. The proposed flow now offers Continue shopping from both empty and non-empty carts. This does not submit an order or alter saved cart contents.

See the [process walkthrough record](future-state-walkthrough.md) for scenarios discussed and remaining limitations.

## Diagram review and next step

The existing diagram represents an earlier process revision. Its sources and PNG exports have not been updated as part of this written reconciliation and must not be treated as equivalent to requirements v0.3.

Required diagram changes:

- Replace minimum-only validation with the 1-to-10 rule and matching error message.
- Align successful-update wording with "Quantity updated successfully."
- Expand the unknown-update placeholder to show section 4's status-check branches and affected-item restrictions, keeping unresolved prolonged recovery explicit.
- Add or reference merging, retention, price refresh and logout boundaries; keep logout security scope and removal recovery open.
- Preserve loading failure, empty-cart confirmation, Continue shopping from both cart states, and last-item removal.
- Regenerate readable exports and review connector attachments after editing the source. No visual revision or visual QA is claimed here.

Review the draft with business, development, and testing roles before baselining requirements. The diagram should retain the load-failure path, validation path, confirmed save/removal failures, and last-item removal path.

## Diagram files

See the [three-page diagram and previews](future-state-diagrams.md) for the earlier cart review, update and removal draft. Use this written v0.3 reconciliation and requirements v0.3 to review discrepancies; neither is an approved implementation baseline.
