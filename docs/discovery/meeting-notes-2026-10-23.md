# Simulated discovery meeting notes

**Date:** 23 October 2026  
**Status:** Draft for sponsor confirmation  
**My role:** I acted as the BA, with AI-assisted documentation.

## Purpose

Document current-state observations, scope agreed during the  discussion, clarifications, and open items for the ShopStack shopping journey.

## Problem and current-state observations

Customers have no visible cart screen to review selected items, quantities, or totals and no interface to complete an order.

Authentication is required before adding items. This is an agreed rule for the proposed release, rather than a confirmed cause of customer abandonment. The current interface has a login form but no registration screen.

No baseline abandonment, conversion, or checkout completion data has been established. Customer behaviour impacts remain hypotheses.

## Desired outcome

Customers should be able to register or log in, add products, review and manage their cart, and submit a demo order with CAD pricing and a clear confirmation.

## Included scope

- Registration and login; authentication required before adding items.
- Cart review showing selected items, quantity per item, unit prices, line totals, and subtotal.
- Quantity updates and item removal before order submission.
- Explicit CAD pricing across catalog, cart, and confirmation.
- Demo order submission and confirmation.

## Excluded scope

- Real payment processing, live payment gateway integrations, and monetary transactions.
- Shipping calculations, physical address validation, and fulfilment workflows.

## Clarifications received in the simulation

- Display prices in Canadian dollars (CAD).
- Successful demo order confirmation should show the order reference, status, item names, quantities, unit prices, and total.
- Confirmation must explicitly state that no payment was taken and no shipping is arranged.
- Retaining item-level order details is a requirement implication to review during requirements and solution design; do not assume the current database already supports it.

## Future improvement proposed for evaluation

Allow adding items without authentication and potentially checking out as a guest. Guest cart and guest checkout are proposals, not approved release scope. Browsing without authentication already exists.

## Open questions and proposed actions

No action owners or deadlines have been agreed.

| ID | Open question | Proposed next action | Status |
|---|---|---|---|
| Q-01 | How will checkout completion be defined and measured? | Agree the completion event and metric definition, identify data collection needs, establish a baseline, then agree an improvement target where appropriate. | Open |
| Q-02 | Does the demo total include only item prices, and how should tax and shipping exclusions be communicated? | Confirm calculation rules and customer-facing wording before requirements are finalized. | Open |
| Q-03 | Is inventory reservation relevant to this release? | Confirm whether inventory belongs in scope before defining stock checks or reservation behaviour. This question does not authorize inventory functionality. | Open |

## Next activity

Document the current customer journey as a numbered sequence, including decisions, system responses, and where the journey stops before creating the current-state process diagram.
