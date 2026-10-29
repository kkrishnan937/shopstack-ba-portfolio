# Cart-read information contract

**Version:** 0.1  
**Date:** 28 October 2026  
**Status:** Draft information contract; backend/schema review pending

## Purpose and boundaries

**Implemented subset:** The [executed read-only slice](../testing/cart-view-executed-2026-10-28.md) now provides cart identity/version, active/empty/expired state, reason, line IDs/product IDs/names/quantities and backend-authoritative integer-cent amounts. Authentication errors return 401, read failures 503, and successful reads use no-store responses. Variant identity, price-change history and mutation/version-conflict guarantees remain unresolved; the inventory below is broader than this implementation. The linked run records actual coverage rather than implying the entire draft contract is complete.

Defines the information and behaviour needed by the dedicated cart page under [requirements v0.4](cart-requirements.md) and [CR-CART-01](cart-readiness-change-and-handoff.md). This is not an implemented API schema or technical sign-off. Exact field names, JSON structure, response codes, cache policy and version semantics require agreement. No API calls, schema changes or application tests were performed in preparing this document.

The previously inspected application has authenticated `GET /api/cart` returning line IDs, product names, prices and quantities. It does not establish the cart identity/version, expiry flag or server-calculated amounts described here. A separate cart record, variants and lifecycle metadata may require model changes; do not assume they already exist.

## Proposed information inventory

These are semantic fields for review, not finalized wire-format names. All amounts are backend-calculated integer cents. The client formats values as CAD with two decimal places and does not become the authoritative calculator.

| Information | Purpose / proposed meaning | Review needs |
|---|---|---|
| Cart identity | Identify the authenticated customer's cart, including empty/expired lifecycle states. | Define creation/lifetime and how no existing cart is represented. Never infer authorization from a supplied identity alone. |
| Current cart version | Identify the state read, for later conflict handling on mutations. | Define type, initialization, increment triggers and how expiry/price changes affect it. Return a version consistently across successful states once semantics are agreed. |
| Cart state | Distinguish active non-empty, ordinary empty and expired. | A state field and expiry flag may overlap; choose one consistent representation rather than contradictory independent values. |
| Currency | CAD for this case study. | Backend and client agree representation; never infer currency merely from a dollar symbol. |
| Item list | Active saved lines belonging to the authenticated customer. | Empty/expired states have no active lines. Define unavailable/deleted product handling separately. |
| Cart-line identity | Distinguish the saved line from the catalog product. | Define identity across merges/removal and any migration. |
| Product/variant identity and display names | Associate quantities/prices/notices with the correct selection. | Existing variant model is unverified; decide how unvaried products are represented. |
| Quantity | Saved whole-number units per line. | Product/variant limit and legacy invalid data need server-side handling; do not assume existing data already complies. |
| Unit price in cents | Current backend-authoritative price used for the read's calculations. | Agree catalog-price consistency and price-change reporting. |
| Line total in cents | Backend-calculated quantity times unit price. | Example: 2 times 1250 cents = 2500 cents. |
| Subtotal in cents | Backend-calculated sum of line amounts, excluding checkout tax/shipping. | Zero for ordinary empty and expired responses. Define safe numeric range/serialization before implementation. |
| Expiry reason indicator | Reflect stored cart-expiry reason, not token expiry. | Must survive repeat visits until successful addition; exact field/schema and persistence mechanism remain open. |
| Previous/current price-change information | Support required increase/decrease notices associated with the affected line. | Old-price source, comparison baseline and notice lifetime remain unspecified; do not invent previous prices in the client. |

Whether timestamps or additional metadata are returned is a technical contract decision, not a new user-facing requirement here. The authoritative response should be a coherent snapshot so quantities, amounts and version do not contradict each other; consistency mechanism requires technical review.

## Response situations and presentation

| Situation | Required information / outcome | Customer presentation and next action |
|---|---|---|
| Active cart | Successful retrieval of owned active lines, identities/version, CAD unit/line/subtotal amounts. No active expiry reason after a successful new addition. | Show selections and server-authoritative amounts. Offer available cart actions subject to unresolved-request restrictions. |
| Ordinary empty | Successful retrieval, no active lines, subtotal 0 cents; no stored expiry reason. | Cart is empty; CAD 0.00; Continue shopping. |
| Expired cart | Successful retrieval, no active expired items, subtotal 0 cents and persisted expiry reason with agreed identity/version representation. | Explain saved cart expired after 30 days without changes; CAD 0.00; Continue shopping. View-local dismissal hides only the notice, not the stored reason. |
| Expired login token | Authentication error, distinct from cart contents/retention state; do not fabricate an empty success response. | Require sign-in before protected changes. Do not show cart-expiry or confirmed-empty feedback merely because authentication failed. Reconciliation of already-submitted requests remains a separate contract. |
| Retrieval failure | Failure distinguishable from successful empty/expired retrieval, with safe customer-facing error information. | Couldn't load your cart. Please try again.; Retry retrieves again without adding, updating or removing items. No confirmed zero/empty claim. |

## Expiry reason and view-local dismissal

- An empty item list alone cannot identify the cause. Return an explicit state/reason representation consistent with the stored flag.
- Actual cart expiry is governed by the 30-times-24-hour policy and exact boundary. Token lapse does not remove items or create this reason.
- Dismissal affects the current view only and must not clear the server flag. Refresh, later views and sign-in must not permanently clear it.
- Failed addition leaves the reason intact. First successful addition clears it; removing that newly added item before another expiry results in ordinary empty state without reviving the old reason.
- This does not add a general mutation to the read-only Retry action. Expiry enforcement/cleanup is server lifecycle processing; whether a read performs lazy expiry cleanup is an open technical choice. Never treat expired contents as active while waiting for cleanup.
- Define the current-view lifecycle and refresh behaviour precisely before coding dismissal; no additional rule is silently selected here.

## Draft contract checks for review

Working references below are contract-review checks, not newly approved CART-AC IDs or executed tests.

| Reference | Proposed verification |
|---|---|
| CON-01 | F2 returns quantities 2/1, unit amounts 1250/2499, line amounts 2500/2499, subtotal 4999 and currency CAD, with a coherent identity/version. |
| CON-02 | Ordinary empty returns no active lines, 0 subtotal and no expiry reason; expired returns no active lines and 0 subtotal with an explicit persisted reason. |
| CON-03 | Token-expiry response cannot be mistaken for either successful empty state; login expiry alone does not set the expiry flag or delete the saved cart. |
| CON-04 | Repeated reads/retry do not perform additions, quantity updates or removals; they do not reset retention or permanently clear the expiry reason. Test setup excludes an actual scheduled expiry unless testing that lifecycle explicitly. |
| CON-05 | Dismissing the explanation makes no server flag-clearing change. Later views still have the reason until a successful addition; failed additions preserve it; later removal after successful addition does not resurrect it. |
| CON-06 | Current prices, old/new notice data and totals refer to the correct lines and consistent read state. Do not fabricate a new confirmed price on retrieval failure. |

## Technical decisions still open

| Topic | Required agreement |
|---|---|
| Schema / compatibility | Exact request/response fields and codes, old client compatibility, cart record/variant support, numeric serialization, safe error shape and identity lifecycle. |
| Retention flag | Persistent marker storage/lifetime, cleanup interaction, expiry boundary consistency and view dismissal design. |
| Version / reconciliation | Version changes, stale-conflict response, idempotency-key scope/result retention and authorized access after token expiry. Do not use cart version alone as proof an old request has stopped. |
| Price notices | Where prior prices are held and when comparison/notice state resets; preserve backend authority and privacy/retention constraints. |
| Cache and freshness | How authorized reads, cache behaviour and version evidence support the agreed freshness/persistence verification. |
| Error/auth UI | Exact authentication-expiry and retrieval error responses and recovery interactions; do not conflate a failed read with a failed mutation. |

Simulated assessment owner: Backend Lead, Sprint 1, under CR-CART-01. This is not an actual assignment, estimate or calendar deadline. New contract checks must be reviewed and traced into requirements and UAT before claiming coverage. Existing execution statuses remain unchanged.

Next: review the semantic inventory and unresolved choices with backend/testing roles, agree an implementable response schema, expand acceptance tests, and assess the cart-viewing slice. This draft alone does not unblock shipment of mutations or implement the API.
