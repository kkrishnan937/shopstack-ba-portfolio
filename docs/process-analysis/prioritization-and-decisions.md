# ShopStack — Prioritization and Decision Record

**Prepared by:** Kailas Krishnan  
**Date:** 23 October 2026  
**Version:** 0.1  
**Status:** Working priorities; first-increment direction recorded; logout scope pending

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
