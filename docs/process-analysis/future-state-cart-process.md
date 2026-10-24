# ShopStack — Future-State Cart Process

**Prepared by:** Kailas Krishnan  
**Date:** 24 October 2026  
**Version:** 0.1  
**Status:** Proposed process — draft for review

## Purpose and boundaries

Define how existing signed-in customers will review and manage their cart in the first increment. The process addresses [GAP-02 and GAP-03](gap-register.md), following [DEC-01](prioritization-and-decisions.md).

The customer is already signed in. Registration and demo order submission remain part of the wider release rather than this increment. Logout scope remains pending. This draft describes intended behaviour, not implemented functionality or completed acceptance testing.

## Proposed entry and exit

- Entry: A signed-in customer requests to view their cart.
- Exit: The customer leaves the cart to continue shopping or closes the cart view. Closing a side panel applies only if that design is selected.
- Customers may review the cart and repeat quantity updates or removals while remaining in the cart view.
- A View cart button and a side panel on the catalog page are candidate design choices, pending wireframe review.

## 1. Open and load the cart

1. Customer requests to view the cart.
2. System attempts to retrieve the customer's saved cart.
3. Decision: **Did the cart load successfully?**
   - No: Display “Couldn’t load your cart. Please try again.” Do not describe the cart as empty. A retry requests the cart again, returning to step 2.
   - Yes: Continue to step 4.
4. Decision: **Is the cart empty?**
   - Yes: Display “Cart is empty,” subtotal **CAD 0.00**, and a **Continue shopping** action that returns the customer to product browsing.
   - No: Display product names, quantities, unit prices, line totals, and the cart subtotal in CAD. Provide quantity-update and item-removal actions.

The contents are unknown when loading fails. An empty-cart message is appropriate only after successful retrieval confirms no items.

## 2. Update quantity

1. Customer enters a new quantity for an existing cart line.
2. Decision: **Is the quantity a whole number of 1 or more?**
   - No: Display “Enter a whole number of 1 or more.” Do not change saved quantities or totals. Allow correction and another attempt.
   - Yes: Attempt to save the requested quantity.
3. Decision: **Was the quantity update saved successfully?**
   - Yes: Display the saved quantity, recalculate that product's line total and the cart subtotal, and display “Update successful.” Return to cart review.
   - Confirmed failure: Display “Update failed. Please try again.” Restore the last confirmed saved quantity, line total, and subtotal; allow another attempt.
   - Outcome unknown: Do not show success or assert that the previous values are current. See the recovery question below; this exception needs a reviewed rule.

Changing quantity alone does not change the unit price. Quantity zero is rejected under the proposed rule; removing the product uses the separate Remove action.

## 3. Remove an item

1. Customer selects Remove for a cart line.
2. System attempts to remove that line from the saved cart.
3. Decision: **Was the item removed successfully?**
   - Confirmed failure: Keep the item, quantity, and subtotal unchanged. Display “Item removal failed. Please try again.” Allow another attempt.
   - Outcome unknown: Do not claim that removal succeeded or failed. See the recovery question below.
   - Yes: Remove the entire line from the displayed cart, recalculate the subtotal, and display “Item removed successfully.” Continue to step 4.
4. Decision: **Is the cart empty?**
   - No: Show the remaining items and recalculated subtotal. Return to cart review.
   - Yes: Show “Cart is empty,” subtotal **CAD 0.00**, and Continue shopping.

## Proposed business rules for review

| ID | Rule |
|---|---|
| BR-CART-01 | Quantity is a whole number of at least 1 for the individually sold products in this increment. |
| BR-CART-02 | Removing a product removes its entire cart line; zero is not an alternative removal action. |
| BR-CART-03 | Product line total equals quantity multiplied by unit price. Cart subtotal equals the sum of product line totals. |
| BR-CART-04 | Display currency explicitly as CAD and monetary values with two decimal places. |
| BR-CART-05 | Show success only after the requested change has been confirmed successful. |
| BR-CART-06 | An invalid quantity must not change saved quantities or totals. |
| BR-CART-07 | Cart retrieval failure must not be represented as an empty cart. |

## Worked calculation

With mugs priced at CAD 12.50 each and one mouse at CAD 24.99:

- Two mugs: line total CAD 25.00; cart subtotal CAD 49.99.
- Change mugs to three: unit price remains CAD 12.50; mug line total becomes CAD 37.50; cart subtotal becomes CAD 62.49.
- Remove the mug line: only the mouse remains; subtotal becomes CAD 24.99.
- Remove the mouse: cart is empty; subtotal becomes CAD 0.00.

These are item-price subtotals, not a decision about a tax-inclusive final total. Tax treatment remains unresolved.

## Open questions and review needs

| ID | Question / review need | Status |
|---|---|---|
| FS-Q-01 | Should the demo calculate tax or display item-price subtotals only? Confirm the customer-facing explanation of tax/shipping exclusions. | Open; sponsor clarification required |
| FS-Q-02 | If a response is lost after an update or removal, how will the system retrieve and present confirmed cart state before permitting a safe retry? What happens if retrieval also fails? | Open; technical and business review required |
| FS-Q-03 | Confirm the cart entry control and whether a side panel or another layout best supports review and editing. | Proposed design; wireframe review pending |
| FS-Q-04 | Does logout belong in the release and, if so, which increment? | Open; scope decision pending |
| FS-Q-05 | Define behaviour when authentication expires while viewing or changing the cart. | Open; further scenario discovery required |
| FS-Q-06 | Confirm whether quantity limits, stock rules, duplicate product lines, or changing catalog prices affect this increment. | Open; further business-rule discovery required |

## Diagram preparation and next step

Draw the opening flow first: request cart → attempt load → loading decision → empty-cart decision → either continue shopping or review/manage items. From cart review, branch into quantity update and removal, returning after a confirmed result. Keep unresolved recovery behaviour visibly marked for review rather than inventing a decision.

Review the draft with business, development, and testing roles before baselining requirements. The diagram should retain the load-failure path, validation path, confirmed save/removal failures, and last-item removal path.
