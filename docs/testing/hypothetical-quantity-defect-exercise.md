# Quantity-update defect lifecycle: training example

**Date:** 28 October 2026  
**Status:** Hypothetical exercise only; no observed defect, implemented fix or executed retest  
**Example ID:** EX-DEF-01

## Evidence boundary

This document records a simulated discussion about reporting and managing a quantity-persistence defect. It is not an entry in an actual application defect log. No screenshots of this mismatch, affected build, measured occurrence rate, root cause or test results exist. Do not treat illustrative expected/actual values as observed results.

The actual application readiness finding remains [BLK-CART-01](cart-loading-readiness-2026-10-28.md): the cart view/retry flow is not implemented and the application scenarios could not proceed. This example does not change any traceability test status to Fail or Pass.

## Proposed successful-update test

Related requirement: CART-FR-02. CART-AC-11 supplies a related successful-update criterion with a different, multi-item fixture; this exercise uses only two mugs. An explicit single-line quantity-3 persistence criterion still requires review before baseline. See [requirements](../requirements/cart-requirements.md) and the [traceability matrix](../requirements/cart-traceability-matrix.md).

Preconditions for future execution: isolated test environment, identified build, valid synthetic authenticated customer, only two saved mugs at CAD 12.50 each, unchanged catalog prices and active cart retention.

1. Open the cart and confirm the starting quantity is 2 and subtotal CAD 25.00.
2. Change quantity to 3 and select Update quantity.
3. Verify quantity 3, line total/subtotal CAD 37.50 and "Quantity updated successfully."
4. Reopen the cart in a way that retrieves fresh saved data. Verify quantity 3 and the same totals persist.

These are proposed test steps, not executed evidence. Fresh retrieval checks persistence rather than only the immediate screen response.

## Hypothetical defect report

| Field | Training example |
|---|---|
| Summary | After updating quantity from 2 to 3, the system shows success, but reopening the cart displays 2 instead of 3. |
| Expected | The saved quantity is 3; reopening displays 3 and line/subtotal CAD 37.50. |
| Hypothetical actual | A success message appears, but reopening displays quantity 2. Reopened totals were not specified; inspect and record them during any real reproduction rather than inventing a result. |
| Execution outcome if observed | Fail: behaviour contradicts the expected persistence outcome. This exercise itself remains Not executed. |
| Business impact | Customers could believe the requested quantity was saved. An unintended quantity might reach later order submission, but that downstream behaviour has not been demonstrated and is outside the first increment. |
| Severity | High, provisional; review against the team's severity definitions and actual evidence. |
| Severity assumptions | Occurrence rate, affected products/users, whether retry works and downstream order impact are unconfirmed. Reopening may reveal the mismatch, but a reliable correction workaround is not established. |
| Priority | Simulated product-owner recommendation: high priority, resolve before releasing quantity updates, and review displaced work with the team. Not an actual release decision. |
| Evidence needed | Starting cart data, exact steps, success-message capture, reopened quantity capture, environment/build, test date and reproducibility details. Use synthetic data; exclude credentials and tokens. |
| Owner / estimate | No actual assignee or estimate. |

## Questions practised and simulated responses

- **Priority:** How urgently should this be fixed compared with other planned work? Simulated product owner prioritizes it before quantity-update release.
- **Investigation:** What investigation is needed before estimating the fix? Reproduce, trace the update request/response and subsequent retrieval, and determine whether saving failed, success feedback was incorrect or retrieval was stale. These are hypotheses, not established causes.
- **Retest scope:** What needs retesting, and which related behaviours might be affected? Repeat the original sequence with fresh retrieval, verify quantities/totals and review boundary quantities, invalid inputs, confirmed failures and duplicate-update risks. Select final regression scope based on the actual fix and impact assessment.
- **Closure:** What evidence is required before closing? Identify the fixed build, record steps and expected/actual results, capture persistent saved quantity, and attach required regression results under the agreed workflow.

## Lifecycle and closure conditions

In a real team, record the issue, reproduce and triage it, agree severity/priority, investigate, implement a fix, retest and review regression evidence. Failed retesting returns the issue for further work. A developer saying "fixed" is not acceptance evidence, and a Git push alone does not close a defect.

This example has not entered that actual workflow: it is neither Open, Fixed nor Closed as an application defect. No implementation was requested or performed through this exercise. Actual execution must supply the missing build, data and evidence before any real defect claim or closure decision.
