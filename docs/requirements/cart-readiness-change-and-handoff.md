# Readiness decisions and cart implementation handoff

**Reference:** CR-CART-01  
**Date:** 28 October 2026  
**Status:** Portfolio-author decisions recorded; technical review and criteria expansion pending

## Authority and scope

Source: the portfolio author's six-row readiness table in the learning discussion. These direct decisions supersede conflicting earlier proposals within the case study. They are not independent client approval, actual staff assignments, estimates or completed implementation. [Requirements v0.4](cart-requirements.md) incorporates the constraints; the existing 37 criteria are not exhaustive coverage of the additions.

## Decisions and delivery impact

| Topic | Recorded decision | Required delivery work |
|---|---|---|
| Layout | Dedicated cart page, readable on phones. | Specify entry/navigation and review responsive, keyboard and focus behaviour. |
| Cart amounts | Backend calculates all amounts in integer cents; client only formats CAD with two decimals. Cart shows subtotal only, alongside its existing line details. | Return authoritative prices, line amounts and subtotal. The previously inspected read endpoint supplies prices/quantities without calculated totals; response/schema and implementation changes are needed. |
| Wider checkout | Tax and shipping calculated at checkout, rounded half-up once per order. | Explicit scope change from their earlier exclusion. Define rates, bases, tax/shipping interaction and precise aggregate rounding sequence before implementation. Do not assume a jurisdiction or shipping method. Real payment and physical fulfilment remain excluded. |
| Session expiry | Token lapse requires sign-in before protected changes; server cart retained. | Distinguish login expiry from cart expiry in API, UI and tests. Session expiry must not trigger a cart-expiry explanation. |
| Submitted requests | Backend reconciles updates submitted before expiry using an idempotency key and cart version. Stale versions return conflict; client refetches before retrying. | Define key scope/lifetime, result replay, authorization for reconciliation, version increments and safe retry. Refetch is necessary but does not alone prove an unresolved request has stopped; do not blindly repeat mutations. |
| Cart expiry and explanation | Server removes items after retention; reason flag stored on cart record. Show only for cart expiry. Dismiss hides only for current view. First successful addition clears flag; failed additions, refresh, sign-in and repeat visits do not. Later removal shows ordinary empty state. | Add flag lifecycle and view-local dismissal criteria. Confirm exact-boundary enforcement, cleanup/read consistency, in-flight interactions and what starts a new view. Dismissal is not a server cart mutation. |
| Shipment gate | No cart mutations ship until session-expiry reconciliation, logout invalidation and retention response contract close. | Track these gates independently of development progress and estimates. Retention enforcement remains a release dependency. Other unresolved release risks are not implicitly waived. |

The author designated a surviving token after logout as a security defect under the required guarantee. The inspected application has no logout/revocation implementation; this record does not claim an observed exploit or executed security test. Invalidation is now required scope; design and evidence remain open.

## Open assessments and simulated targets

| Item | Simulated owner | Simulated target | Closure evidence required |
|---|---|---|---|
| Logout invalidation: release blocker | Backend/Security | Sprint 1 | Define scope/failure behaviour and active-request boundary; implement and verify token cannot authorize subsequent protected requests after successful logout. |
| Exact retention response contract | Backend Lead | Sprint 1 | Reviewed active/empty/expired/authentication-error/retrieval-failure contract, persistent expiry reason and authoritative amount representation. |
| Prolonged recovery UX | Product/UX | Sprint 2 | Agreed messages, next actions and escalation consistent with backend guarantees. A UX timeout cannot itself prove cancellation or safely unlock editing. |

These are relative exercise targets, not named actual assignees, dated sprints or estimates. Do not infer dates from earlier simulated sprint examples. Backend input remains necessary for prolonged recovery even though Product/UX owns its proposed customer experience.

## First implementation slice handoff

**Outcome:** Review a synthetic signed-in customer's saved cart through a dedicated page and recover from retrieval failures without mutations.

**Included:** View cart entry/navigation, responsive line details and authoritative CAD subtotal, confirmed empty/expired explanations, view-local dismissal where specified, loading/error handling, Retry, Continue shopping and accurate demo pricing wording. Provide isolated backend/database, synthetic data and reversible cart-read failure support.

**Separate development:** Quantity changes, removal, merging, retention and logout, with estimates and integration dependencies visible. No mutation shipment before the recorded gates close. No checkout tax/shipping implementation follows from this read-only slice alone.

**Readiness inputs:** Assess backend calculations/contract, retention response, dedicated-page and dismissal designs, authentication handling, fixtures and evidence access. Separate cart-view, retention, session reconciliation, logout and integration estimates; state overlap and assumptions. No estimate is established.

**Verification:** CART-AC-01 through CART-AC-07 supply existing read-only expectations, with CART-AC-07 updated in v0.4; CART-AC-28/36 cover expiry presentation and boundaries. Add criteria/tests for authoritative cents, authentication conflicts, idempotency and flag lifecycle. CART-T-04/05 remain actually Blocked under BLK-CART-01 until prerequisites are verified.

## Change impact and next work

- Requirements: v0.4 records constraints; add new acceptance criteria through review rather than claiming the existing 37 cover all additions.
- Traceability/UAT: update the pricing-notice expectation in T-07; retain statuses. Add new families for server amounts, session reconciliation, revocation and flag lifecycle after contract definition.
- Wireframes v0.3: local arithmetic is demonstration only; broad no-tax/shipping wording and missing dismissal/page/authentication states need revision. They do not implement the new backend guarantee.
- Written process/diagrams: add server amount authority, token/cart expiry distinction, conflict/refetch handling and flag lifecycle. Earlier pending-invalidation-scope labels are superseded, but technical implementation remains open.
- Checkout: separately define calculation inputs and once-per-order rounding semantics, estimate scope and plan tests before building it.

Review the read-only API contract and new criteria next, then estimate and implement in isolation. No code or application test execution was performed through this decision update.
