# ShopStack — Prioritization and Decision Record

**Prepared by:** Kailas Krishnan  
**Date:** 23 October 2026  
**Version:** 0.1  
**Status:** Working priorities; first-increment direction and subsequent cart/scope decisions recorded. Earlier entries below retain their historical status; DEC-02 through DEC-07 record the 25 October updates.

## Purpose

Record proposed business priorities, delivery dependencies, and the rationale for the first increment. Business priority describes importance to the release objective; delivery order also considers dependencies and which customers an increment serves.

Related artifacts: [gap register](gap-register.md), [current-state diagram](ShopStack-Current-State-Improved.png), and [discovery notes](../discovery/meeting-notes-2026-10-23.md).

## Prioritization method

MoSCoW categories: Must have — necessary for the agreed release objective; Should have — important with an acceptable temporary workaround; Could have — useful if capacity allows; Won't have this release — deliberately excluded. Priorities below are proposals, not a finalized release baseline. No delivery estimates have been established.

## Proposed priorities

| Gap | Capability | Proposed priority | Rationale | Delivery position / open decision |
|---|---|---|---|---|
| GAP-01 | Registration | Must have | New customers need to create an account because authentication is required before adding items. Existing account holders can already log in. | Remains in complete release scope; scheduled after the first increment, exact sequence pending. |
| GAP-02 | Cart review | Must have | Customers need to verify selected products, quantities, prices, and subtotal before submitting an order. | First increment, together with GAP-03. |
| GAP-03 | Cart management | Must have | Customers need to correct quantities and remove unwanted items. No acceptable correction workaround has been identified in the interface. | First increment, together with GAP-02 so customers can see what they are editing. |
| GAP-04 | Demo order submission and confirmation | Must have | Customers need to submit a demo order and receive confirmation to complete the agreed journey. | Remains in complete release scope; detailed sequence pending. Real payments and shipping remain excluded. |
| GAP-05 | Logout | Must have — proposed, subject to scope confirmation | Customers need to end their session at any time; a shared browser presents a risk of unauthorized session use. No actual misuse has been established. | Newly identified need; inclusion, priority, and delivery position require a sponsor decision. |

## DEC-01 — First increment

| Field | Record |
|---|---|
| Decision | Focus on existing account holders and deliver cart review and cart management together in the first increment. |
| Basis | Sponsor direction during the discovery/prioritization exercise; not a conclusion established by customer metrics. |
| Reason for grouping | Customers need to see products and their quantities before updating quantities or removing unwanted items. |
| Customer outcome | Existing account holders can inspect and correct their selections. |
| Remaining release scope | Registration and demo order submission/confirmation remain planned for the complete release. |
| Increment limitations | The first increment does not enable new account creation or complete order submission. Logout scope is unresolved. |
| Missing evidence | Reliable visitor-segmentation data and support records are unavailable. |
| Effect on confidence | Cart improvement may be useful, but there is insufficient evidence to confirm it addresses the most important customer need. |
| Follow-up | Collect visitor and support information, then check whether the delivery order should change. |
| Review trigger | New evidence indicates a different customer need should take precedence, or dependency/feasibility findings materially affect the proposed increment. |

## Open actions

| ID | Action | Owner | Status |
|---|---|---|---|
| ACT-01 | Identify an available, appropriate source of visitor-segmentation data and support feedback; assess its reliability. | To be assigned | Open |
| ACT-02 | Review new evidence against DEC-01 and record any change to delivery order. | To be assigned | Open; dependent on ACT-01 |
| ACT-03 | Confirm logout scope and priority. | Sponsor role; assignment pending | Open |
| ACT-04 | Assess implementation dependencies and estimates before committing to a delivery schedule. | Delivery team role; assignment pending | Open |

## Next activity

Define the proposed future-state process for cart review and management, including quantity changes, item removal, empty-cart behaviour, and exceptions. Proposed rules need review before becoming requirements.

## Cart rule decisions — 25 October 2026

Source: discussion with the portfolio author in the simulated business analysis exercise. These are case-study decisions, not independent stakeholder approval, implemented behaviour, or executed UAT. The original process draft predates these decisions and still requires reconciliation.

| ID | Decision | Rationale / boundary |
|---|---|---|
| DEC-02 | Retain an account's saved cart for 30 days after its last successful addition, quantity update, or removal. After 30 days without a successful change, clear the contents and explain that the saved cart expired. | Confirmed by the portfolio author. Login expiry does not clear the cart. This is an application retention rule, independent of browser cache expiry; it is not attributed to Walmart. Viewing or refreshing alone does not extend retention. |
| DEC-03 | Merge additions of the identical product and variant into one cart line: two units plus one becomes three. Different designs/variants remain separate lines. | Confirmed by the portfolio author. Price differences alone do not establish a different product identity. |
| DEC-04 | Permit whole-number quantities from 1 to 10 per product/variant, including the combined quantity after repeated additions. Reject requests that exceed 10 and preserve saved quantities and totals. Suggested message: "Enter a whole number from 1 to 10." | Confirmed demo purchase limit. Inventory data is unavailable; the limit does not establish stock availability or reserve inventory. Any increase requires review with relevant inventory evidence. |

### DEC-05 — Demo pricing boundary

Confirmed by the portfolio author on 25 October 2026 during the simulated analysis exercise: display item-price subtotals only, in CAD with two decimal places. Calculate each line as unit price multiplied by quantity and the subtotal as the sum of line totals. Do not calculate tax or shipping in this demo. Display: "Demo only—tax and shipping are not calculated. No payment is taken." Demo order confirmation must also state that no shipping is arranged. This is an agreed demo scope decision, not a statement about applicable real-world tax obligations. Implementation and verification remain pending.

### DEC-06 — Logout in the first increment

Confirmed by the portfolio author on 25 October 2026 during the simulated analysis exercise: include logout as a Must have in the first increment, alongside cart review and management for existing account holders. Customers must be able to end their signed-in session. Logout retains the account's saved cart under DEC-02; it neither clears the cart nor extends its retention period. Protected cart changes require authentication again after logout. Detailed session termination behaviour requires technical review and acceptance criteria. This decision resolves the earlier pending logout scope and priority entries (GAP-05 / ACT-03); those historical entries describe the earlier state. Implementation and UAT remain pending.

### DEC-07 — Inventory boundary

Confirmed by the portfolio author on 25 October 2026 during the simulated analysis exercise: exclude stock availability checks and inventory reservation from this demo release. The 10-unit limit in DEC-04 is a purchase rule, not a guarantee of availability. Adding or retaining a cart item does not reserve stock. Any future inventory capability requires separate discovery, inventory data, requirements, and a scope decision. This resolves the inventory-in-scope question in the discovery notes and the inventory portion of FS-Q-06; other product and pricing questions require their own disposition. Implementation and UAT remain pending.

### Follow-up

Reconcile these decisions with the future-state process, then derive acceptance criteria for expiry boundaries, login expiry, repeated additions, and quantity limits. Cart recovery and price-change discussions also need consolidation. Implementation and UAT remain pending.
