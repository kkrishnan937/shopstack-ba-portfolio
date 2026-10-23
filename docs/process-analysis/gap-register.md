# ShopStack — Gap Register

**Prepared by:** Kailas Krishnan  
**Date:** 23 October 2026  
**Version:** 0.1  
**Status:** Draft for review

## Purpose

Compare the observed customer journey with the capabilities needed to review selections and submit a demo order. This register supports requirements discovery and scope discussions; identifying a gap does not approve a solution or establish delivery priority.

## Evidence basis

Manual walkthrough of the existing application, including logged-out product browsing, an add-to-cart attempt without authentication, invalid login, valid login, and adding a product after login. The observations concern the customer interface. Success messages alone do not independently verify database contents.

Supporting artifacts:

- [Discovery meeting notes](../discovery/meeting-notes-2026-10-23.md)
- [Current-state process diagram](ShopStack-Current-State-Improved.png)
- [Editable process diagram](ShopStack-Current-State-Improved.drawio)

## Gaps

| ID | Current state | Needed capability | Gap | Effect on the customer's task | Evidence |
|---|---|---|---|---|---|
| GAP-01 | Login is available, but no registration option is visible. | New customers can create an account. | No customer-facing registration capability. | New customers cannot create an account through the interface and proceed to authenticated shopping. | Manual walkthrough: login form visible; no registration option found. |
| GAP-02 | After adding a product, the system displays “Added to cart,” but no cart review option is visible. | Customers can review selected products, quantities, unit prices, line totals, and subtotal. | No customer-facing cart review capability. | Customers cannot verify their selections or review the subtotal before order submission. | Manual walkthrough: “Added to cart” message observed; no cart review option found. |
| GAP-03 | The interface provides Add to cart buttons, but no quantity-update or item-removal controls. | Customers can change quantities and remove unwanted items before submitting an order. | No customer-facing cart management capability. | Customers cannot correct quantities or remove unwanted selections through the interface. | Manual walkthrough: Add to cart buttons observed; no quantity-update or removal controls found. |
| GAP-04 | After adding a product, the system displays “Added to cart,” but provides no checkout or order-submission option. | Customers can submit a demo order and receive confirmation. | No customer-facing demo order submission or confirmation capability. | Customers cannot complete an order submission through the interface. | Manual walkthrough: “Added to cart” observed; no checkout or order-submission option found. |
| GAP-05 | The interface shows a logged-in status but no logout control. | Customers can end their signed-in session. | No customer-facing logout capability. | Customers cannot log out through the application interface. | Manual walkthrough: while logged in, no logout option was visible on the page. |

## Scope and review status

| Gap | Relationship to discovery scope | Review status |
|---|---|---|
| GAP-01 | Registration included in discovery scope. | Must have proposed; detailed requirements pending. |
| GAP-02 | Cart review included in discovery scope. | Detailed requirements and priority to be reviewed. |
| GAP-03 | Quantity updates and item removal included in discovery scope. | Detailed requirements and priority to be reviewed. |
| GAP-04 | Demo order submission and confirmation included; real payments and shipping excluded. | Detailed requirements and priority to be reviewed. |
| GAP-05 | Newly identified need; logout was not explicitly included in the discovery scope. | Must have proposed; sponsor scope and priority decision still required. |

## Interpretation and limitations

- Customer task limitations are supported by the walkthrough. Abandonment, lost sales, conversion changes, and time savings have not been measured.
- These gaps describe customer-facing capabilities; they do not imply that every supporting backend capability is absent.
- Needed capabilities do not prescribe separate pages, particular buttons, or a technical solution.
- Gap IDs in this register are its reference identifiers. Future requirements should link to them explicitly.
- Successful add-to-cart behaviour was observed. Other API failures and session-expiry scenarios require further investigation.

## Open review items

1. Confirm whether logout belongs in the release scope and establish its priority.
2. Define checkout completion, data collection, and the baseline before agreeing improvement targets.
3. Confirm demo total calculation rules and the wording for tax and shipping exclusions.
4. Resolve whether inventory-related behaviour belongs in scope before specifying it.

## Next step

See the [prioritization and decision record](prioritization-and-decisions.md) for proposed priorities and the first-increment direction. Develop the future-state cart review and management process; keep unresolved scope and business-rule questions open.
