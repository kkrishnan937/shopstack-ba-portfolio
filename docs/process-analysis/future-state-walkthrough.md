# ShopStack — Future-State Process Walkthrough

**Prepared by:** Kailas Krishnan  
**Recorded:** 25 October 2026  
**Version:** 0.1  
**Status:** Draft review record; open recovery and business rules remain

## Purpose and method

Review the [proposed cart process](future-state-cart-process.md) by following example customer scenarios through its decisions and outcomes. The walkthrough used discussion and diagram tracing, including corrections and hints. It did not execute implemented cart functionality, establish independent stakeholder approval, or constitute UAT.

## Scenarios discussed

| ID | Scenario | Expected route / result | Walkthrough observation |
|---|---|---|---|
| PW-01 | Cart loads; quantity changes from two mugs to three and saves successfully. | Load Yes → empty No → valid quantity Yes → save Yes → cart review. Mug line total CAD 37.50; subtotal with one mouse CAD 62.49. | Route and subtotal identified; line-total arithmetic corrected during discussion. |
| PW-02 | Customer enters zero quantity. | Validation No → explain whole-number minimum of 1 → correction. No save attempt; saved values unchanged. | Invalid-input response and unchanged values identified. |
| PW-03 | Quantity is valid but saving is confirmed to have failed. | Save No — confirmed failure → failure message and confirmed saved values → quantity entry if customer retries. | Initially confused with input correction/unknown outcome; correct failure response and retry destination subsequently identified. |
| PW-04 | Customer removes the only item successfully. | Removal Yes → empty Yes → CAD 0.00, empty-cart message, Continue shopping. | Expected empty-cart outcome identified after tracing the successful-removal path. |
| PW-05 | Cart retrieval fails. | Load No → load-error message → customer Retry → attempt cart retrieval again. | Failure message and retry destination identified. |
| PW-06 | Valid update receives no response; saved outcome is uncertain. | Unknown → FS-Q-02 recovery placeholder. Do not claim confirmed success or failure. | Explained that saving may occur even when confirmation is delayed or lost. Recovery remains unresolved. |
| PW-07 | Mugs removed successfully while one mouse remains. | Removal Yes → empty No → cart review; subtotal CAD 24.99. | Non-empty return destination, No branch, and subtotal identified through prompts. |
| PW-08 | Mouse removal is confirmed to have failed. | Removal No — confirmed failure → failure message; mouse remains and quantity/subtotal stay unchanged. | Correct failure branch and unchanged-state behaviour identified. |
| PW-09 | Customer with a non-empty cart wishes to continue browsing without changing selections. | Continue shopping → customer selects action → product browsing; saved cart unchanged. | Missing explicit path found during review. User added the connector and action label; visible changes reviewed. |

## Finding and disposition

**FIND-01 — Missing exit from non-empty cart:** The diagram offered update and removal actions but no explicit Continue shopping path for a customer making no changes.

**Disposition:** Added Continue shopping to the non-empty cart's actions and connected it to the existing customer-selection step and product-browsing endpoint. Updated written process v0.2 accordingly. Confirm saved diagram contains the reviewed changes before publishing its next revision.

## Remaining review items

- FS-Q-02: Unknown outcomes have a pending-review placeholder, not an agreed recovery flow. A removal-specific unknown-outcome scenario has not been walked through separately.
- Tax treatment, session expiry, logout scope, and additional cart rules remain open in the written process.
- Initial empty-cart entry has been discussed during process definition; the recorded last-item-removal scenario is not a substitute for a separate entry-path check.
- This review is not an exhaustive scenario set. Requirements review and later UAT will need broader coverage.
- Verify the latest saved diagram, connector attachments, and readable exports before publication.

## Next activity

Clarify unresolved business rules and recovery behaviour with the appropriate business and technical roles. Use the process to develop requirements and acceptance criteria; keep unresolved points explicit rather than treating them as agreed rules.
