# Cart-viewing delivery workshop

**Date:** 28 October 2026  
**Version:** 0.1  
**Status:** Simulated workshop findings; proposed refinements awaiting review

## Purpose and evidence boundary

**Subsequent disposition:** The portfolio author's [CR-CART-01](../requirements/cart-readiness-change-and-handoff.md) records later decisions, including acceptance of the message-lifetime rule plus view-local dismissal, dedicated page and explicit backend constraints. Use that record and requirements v0.4 for current direction; this workshop preserves the earlier proposal history. No technical assessment has actually been performed.

Prepare a small cart-viewing/retry implementation slice without silently changing the complete first-increment release scope. All role statements, assignments and timing below are simulated practice. No developer investigation, estimate, implementation, approval or calendar commitment has occurred through this workshop.

Sources: [requirements v0.3](../requirements/cart-requirements.md), [DEC-02 and DEC-08 retention rules](../process-analysis/prioritization-and-decisions.md), [wireframes](../wireframes/cart-wireframes.md), [traceability matrix](../requirements/cart-traceability-matrix.md) and [actual test-readiness blocker](../testing/cart-loading-readiness-2026-10-28.md).

## Proposed implementation slice

Deliver View cart, names/quantities/prices/line totals/subtotal in CAD, confirmed empty state, cart-loading error, non-mutating Retry, demo pricing notice and Continue shopping. Related criteria: CART-AC-01 through CART-AC-07. Quantity updates, removal and logout remain separate development work, not removed from the complete release.

In the simulation, the product owner allowed retention to be developed separately but required its agreed enforcement in any release containing cart functionality. Expired saved items must not appear as an active cart. This is a proposed sequencing clarification, not an actual release approval. Cart-view development may proceed independently while retention and integration remain release dependencies.

## Capability assessment and estimate inputs

Earlier source inspection of `backend/routes/cart.js` in the application repository found an authenticated cart-read endpoint returning cart-line IDs, product names, prices and quantities. This was source evidence, not runtime proof of working error handling, expiry or retention. Line totals and subtotal were not returned in that inspected endpoint; they can be derived subject to agreed calculation and rounding design.

Before an estimate, confirm the entry/layout choice, calculation/rounding responsibility, authentication-expiry and error responses, retention integration contract, isolated backend/database fixtures and controlled retrieval-failure method. Separate cart-viewing, retention and integration estimates and identify overlap to avoid double counting. No effort estimate has been established.

## Proposed expiry explanation and contract

The existing policy establishes 30 times 24 hours since the last successful cart change, active before expiry and expired at the boundary and afterward. CART-AC-28 and CART-AC-36 require an expiry explanation. They do not yet specify its persistence across visits.

**Proposed refinement from the simulated product owner:** Keep the expiry explanation visible while the cart remains empty because of expiry. Clear it after a successful new addition. Refresh, sign-in and later visits must not clear it. This is not yet an approved requirements revision. A failed addition should not be treated as successful creation of a new active cart; detailed criteria still need review.

**Candidate developer approach:** Return no active items plus an explicit expiry indicator so the UI can distinguish expiry from ordinary emptiness. Retain the reason and clear it after successful addition. No API field name, HTTP status, storage mechanism or response schema has been agreed or implemented. The proposed indicator is not evidence of current endpoint behaviour.

Open questions include how the reason is stored, what constitutes the transition after a new addition, error and concurrency handling, retention/privacy implications of the marker, and how expiry cleanup interacts with it. Do not infer an approved data-retention duration for this marker from the cart contents policy.

## Open technical assessment

| Field | Simulated discussion / actual status |
|---|---|
| Assessment | Inspect existing cart storage/timestamps, cart-read and add-item flows; compare expiry-reason persistence and clearing options. |
| Simulated owner | Developer, with technical lead and tester input. No actual assignee is established. |
| Expected findings | Options, evidence of dependencies, risks, test needs and effect on separate retention/integration estimates. |
| Proposed test topics | Repeat visits and sign-in/refresh preserve the reason; failed addition does not clear it; successful addition clears it. These are candidate cases, not executed tests. |
| Review point | Next refinement; calendar date unconfirmed. This is not an implementation completion date. |
| Current status | Open proposed assessment; no investigation or estimate completed. |

## Follow-up and baseline impact

### Proposed criterion: empty after a new shopping cycle

**Working reference:** EXP-PROP-01; not a baselined CART-AC identifier.

**Given** the customer's cart expired and displayed the expiry explanation, and the customer subsequently added one item successfully, clearing the previous expiry reason,

**when** the customer successfully removes that only item before any new cart expiry,

**then** display "Cart is empty", subtotal CAD 0.00 and Continue shopping; do not restore the previous expiry explanation.

This follows a subsequent simulated product-owner clarification: the successful addition starts a new active cart state; removing that item creates ordinary emptiness rather than resurrecting the old expiry cause. It remains a proposal for review, not an approved rule, implemented behaviour or executed test. Include the transition in future design/test review if the message-lifetime policy is accepted.

Review the message-lifetime proposal with the business and technical roles before adding criteria, changing the API contract or baselining the design. If accepted, version the requirements, wireframe review notes, traceability and UAT cases together. Current requirement/test IDs and actual execution statuses remain unchanged. The existing expiry screen illustrates the message, not its persistence logic.

Keep prolonged unknown-update recovery and logout security guarantees open. No statement in this workshop resolves those separate requirements or unblocks actual UAT.
