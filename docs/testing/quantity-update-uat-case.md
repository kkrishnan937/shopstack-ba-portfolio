# UAT case: successful quantity update

**Case ID:** CART-UAT-01  
**Version:** 0.2
**Prepared:** 28 October 2026  
**Status:** Draft; execution Not run  
**Readiness:** Implementation and environment prerequisites pending

## Purpose and traceability

Verify a successful quantity update, correct totals and consistent values after fresh cart retrieval. Expands planned outline CART-T-11 from the [traceability matrix](../requirements/cart-traceability-matrix.md). Links: GAP-03 -> CART-FR-02 / US-02 -> CART-AC-11 -> normal-cart design concept. The current single-item wireframe does not provide the complete multi-item layout required by this fixture.

The fixture below deliberately matches CART-AC-11: two mugs and one mouse. Its final subtotal is CAD 62.49, unlike the single-line CAD 37.50 example used in the hypothetical defect exercise. Persistence checks are proposed supporting verification of saved quantity; explicitly review that expectation before baselining, rather than silently treating it as a newly approved acceptance criterion.

No steps below have been executed. Simulated developer explanations establish a proposed evidence method, not verified implementation behaviour. See the [actual readiness record](cart-loading-readiness-2026-10-28.md) for the missing cart UI and unavailable backend during the earlier inspection. This case has not undergone a new readiness check or changed CART-T-11's Not run status.

## Preconditions and controlled data

- An isolated test environment and identified application build provide working authentication, cart viewing and quantity updates.
- A synthetic customer is signed in with valid authentication and owns the fixture below.
- The cart is within retention, no other session changes it, and catalog prices stay unchanged during the case.
- Developer/tester has confirmed a safe method to inspect persisted cart data and recognize a fresh, non-cached cart-read response. Do not assume a UI refresh bypasses every cache.
- Failure injection is off; this case tests successful saving, not timeout recovery. No unresolved earlier request affects either item.
- Actual participant responsibilities and business-review arrangements are agreed before execution; no real assignees are established by this document.

| Product | Starting quantity | Unit price | Starting line total |
|---|---|---|---|
| Mug, one identified product/variant | 2 | CAD 12.50 | CAD 25.00 |
| Mouse, one identified product/variant | 1 | CAD 24.99 | CAD 24.99 |

Starting cart subtotal: **CAD 49.99**. Use synthetic identifiers and a resettable fixture. Record the exact product/customer references in restricted test evidence as appropriate; never publish passwords or tokens.

## Execution steps

All actual-result and evidence cells are intentionally blank until execution. A blank actual result is not a pass.

| Step | Action | Expected result | Actual result | Evidence reference |
|---|---|---|---|---|
| 1 | Select View cart. | Both fixture lines appear with quantities 2 and 1, correct unit/line prices and subtotal CAD 49.99. | | |
| 2 | Change the mug quantity to 3 and select Update quantity once. | On confirmed success, mug quantity 3, mug line CAD 37.50, mouse quantity 1 and line CAD 24.99, subtotal CAD 62.49, and "Quantity updated successfully." | | |
| 3 | Developer/tester inspects the isolated environment's persisted cart record for this synthetic customer and mug. | Saved mug quantity is 3; mouse remains 1. Record when the observation was made relative to the successful request. | | |
| 4 | Close/reopen or refresh the cart using the implemented retrieval path, with Network recording enabled by the tester. | A new cart-read request occurs. Verify the response is obtained from the intended backend rather than merely reused from browser cache; record cache indicators and any limitations. No new quantity mutation occurs. | | |
| 5 | Inspect the fresh cart-read response and the reopened cart. | Response and UI both show mug quantity 3 and mouse quantity 1. UI shows unit prices CAD 12.50 / CAD 24.99, line totals CAD 37.50 / CAD 24.99 and subtotal CAD 62.49. Totals need not exist as API fields if the agreed contract supplies data to calculate them. | | |
| 6 | Compare persisted record, read response and UI observations. | Quantities agree across all three. Document any mismatch without assuming its technical cause. | | |

## Evidence and responsibilities

The business reviewer can validate the customer journey and displayed outcome. Developer/tester supports backend/network verification; database access is not a prerequisite for the BA or business reviewer personally.

Capture starting cart, success feedback, reopened cart and sanitized request/response evidence. Correlate backend observations using the synthetic customer/product and execution sequence. A network response alone is not proof of persistence; a database snapshot alone does not prove correct customer feedback. Avoid exporting full network archives containing authentication headers into the public portfolio.

Actual build:  
Environment:  
Execution date/time:  
Tester / business reviewer:  
Technical evidence reviewer:  
Overall actual result:  
Evidence links:  
Defect / blocker links:

## Result rules and cleanup

### Incomplete verification and access limitations

Use only authorized access. If direct persisted-record inspection is unavailable, ask the technical team about an authorized test-support report or independent authenticated backend read. Confirm what the alternative actually proves: a new session helps rule out screen-local state, but a response is not proof of durable persistence unless the retrieval path and evidence are understood. Agree and record an equivalent verification method before substituting it for step 3; do not claim stronger evidence than the method supports.

During actual execution, completed UI or API checks may be individually recorded Pass with evidence. If a required persistence check cannot be performed, record that check as Blocked, explain the access/evidence limitation, and keep the overall case Blocked even if other steps pass. Preserve completed-step evidence and identify the remaining check, proposed resolution, actual follow-up owner and agreed review date. If no owner/date is agreed, mark them unassigned/unconfirmed rather than inventing them. A known failing required check must still be reported; blocking another check must not hide a failure.

Removing a required check or accepting a weaker method needs explicit review of the requirement, evidence limitation and acceptance risk by the appropriate business/testing/technical roles. Update the case version and traceability references after that decision; never silently skip the check or mark the original complete case Pass.

This is a proposed execution policy from simulated review. No UI checks have actually passed, no persistence check has actually been attempted, and this case remains Not run.

- **Not run:** Case has not been attempted; current status.
- **Blocked:** An execution attempt cannot proceed because required UI, environment, fixture or safe evidence access is missing. Record the specific unmet prerequisite and completed steps, if any.
- **Pass:** All required, reviewed expectations are satisfied with recorded execution evidence.
- **Fail:** Executed behaviour contradicts a required expectation. Report expected/actual values and reproducible evidence; do not guess a root cause. The hypothetical defect document is not actual evidence.

After recording results, reset only this synthetic fixture using the agreed method and verify cleanup. Retain sanitized evidence and any defect/retest links. This case does not cover failure recovery, quantity boundaries, invalid inputs, retention-clock reset or concurrent price changes; those require their own linked cases.
