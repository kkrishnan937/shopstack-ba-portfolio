# ShopStack: from cart uncertainty to executed recovery

**Independent BA portfolio case study | 28 October 2026**

## Problem and role

ShopStack's storefront supported browsing, login and add-to-cart requests but offered no cart review. Customers could not verify saved selections or totals. The initial acceptance attempt was [blocked](testing/cart-loading-readiness-2026-10-28.md): the required screen/retry controls were missing and no running backend fixture was available. No customer conversion or financial impact had been measured.

Kailas Krishnan practised the BA role through an independent learning project, with AI-assisted analysis and implementation. Stakeholder conversations were simulated; they are not client interviews or sign-off. The deliverable became a deliberately small read-only cart slice, followed by agent-executed acceptance checks with actual evidence.

## Analysis and decisions

The [gap register](process-analysis/gap-register.md) connected the missing customer capability to [requirements](requirements/cart-requirements.md), [process diagrams](process-analysis/future-state-diagrams.md), [wireframes](wireframes/cart-wireframes.md) and a [traceability matrix](requirements/cart-traceability-matrix.md). A key distinction emerged: retrieval failure does not prove that a cart is empty. Retry must retrieve saved data without adding, updating or removing selections.

The [scope handoff](requirements/cart-readiness-change-and-handoff.md) selected a dedicated mobile-readable cart page, backend-authoritative integer-cent amounts, and separate ordinary-empty, cart-expired and login-expired states. Mutation work was deferred behind explicit gates rather than presenting an unfinished quantity/removal workflow as complete.

## Delivered and verified

[Initial implementation](https://github.com/kkrishnan937/shopstack/pull/1) merged by the repository owner; [review fixes and CI](https://github.com/kkrishnan937/shopstack/pull/2) remain a draft. Production deployment is unconfirmed.

The implemented React page uses actual authentication and Express cart routes, verified on embedded PostgreSQL and PostgreSQL 17. It shows owned selections and CAD totals, offers Continue shopping, handles cart-read errors and Retry, and displays retained expiry explanations. Backend cart/order writes and frontend add controls are disabled in this increment.

The executed fixture contained two mugs at CAD 12.50 and one mouse at CAD 24.99. A controlled backend read failure returned 503; the UI showed its error/Retry without empty-cart or zero-subtotal claims. Retry failed safely while the control remained, then recovered to **CAD 49.99** after removal. Database snapshots confirmed unchanged saved items and retention metadata.

**Results: 9 planned families plus 6 supplemental checks passed on both CI database adapters; 28 planned families remain Not run.** See the [review and execution evidence](testing/cart-review-2026-10-28.md), [failure screenshot](testing/evidence/cart-review-postgres-2026-10-28/01-cart-load-failure.png), [recovered cart](testing/evidence/cart-review-postgres-2026-10-28/03-cart-recovered.png) and [PostgreSQL results](testing/evidence/cart-review-postgres-2026-10-28/run-results.json). Evidence includes source/build fingerprints and persistence checks. The original local readiness blocker is resolved for this slice.

## Limits and lesson

This is agent-executed local/CI acceptance evidence, not independent business approval or production validation. The existing cloud workflow failed at AWS credential configuration. Quantity changes, removal, logout revocation, safe mutation recovery and checkout are not delivered; exact retention boundaries and full accessibility remain unverified. Legacy cart-age migration is an explicit tradeoff.

The principal lesson was to stop at a testable scope: one traced business need, working UI/API/data integration, and reproducible failure/recovery evidence demonstrated more than additional unexecuted documents. Next work should extend that verified path without erasing its boundaries or overstating business results.
