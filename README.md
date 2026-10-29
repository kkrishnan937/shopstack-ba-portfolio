# ShopStack Business Analyst Portfolio

*This project follows a simulated business analysis process.*

**Customer Purchase Journey Improvement**  
**Author:** Kailas Krishnan  
**Status:** Read-only cart slice verified locally and in CI on PostgreSQL 17; wider release incomplete

An independent Business Analyst case study using an existing e-commerce learning application to practise an end-to-end business analysis workflow. This repository will grow as discovery, process analysis, requirements, validation, and evaluation work is completed and reviewed.

**Start here:** [One-page case study](docs/case-study.md) -> [executed acceptance results](docs/testing/cart-view-executed-2026-10-28.md) -> [failure screenshot](docs/testing/evidence/cart-view-2026-10-28/01-cart-load-failure.png) / [recovered cart](docs/testing/evidence/cart-view-2026-10-28/03-cart-recovered.png).

**Actual outcome:** 9 planned cart-view test families and 6 supplemental checks passed locally and in CI on embedded PostgreSQL and PostgreSQL 17; 28 families remain Not run. [Review findings and durable evidence](docs/testing/cart-review-2026-10-28.md). The owner merged [initial PR #1](https://github.com/kkrishnan937/shopstack/pull/1); [follow-up PR #2](https://github.com/kkrishnan937/shopstack/pull/2) remains a draft with passing checks. The existing AWS workflow failed before deployment. No production release or independent sign-off is claimed.

## Business context

[ShopStack](https://github.com/kkrishnan937/shopstack) originally supported catalog browsing, login and add-to-cart requests without cart review. The local implemented slice adds a dedicated cart page with real authentication, server-calculated totals, empty/expired states and safe Retry. Cart/order writes are disabled while mutation gates remain open; checkout is not implemented.

This case study investigates how customers could review their selections and submit a demo order. Customer abandonment, conversion impact, and financial benefits have not been measured.

## Proposed outcome and scope

Enable customers to register or log in, add products, review cart items and totals, update quantities, remove items, and submit a demo order with confirmation. Display prices explicitly in CAD.

The simulated sponsor retained authentication before adding items. Guest cart and guest checkout are future proposals, not agreed release scope.

Real payments and physical shipping/fulfilment remain excluded. Cart shows item-price subtotal only; CR-CART-01 now includes tax/shipping calculation at later demo checkout, with detailed inputs and rounding sequence still to define. No payment is taken or shipping arranged. Stock checks/reservation remain excluded. Logout invalidation is required; its design, session reconciliation and prolonged recovery remain open.

## Portfolio artifacts

| Artifact | Status | Link |
|---|---|---|
| Discovery meeting notes | Draft for simulated sponsor confirmation | [Read meeting notes](docs/discovery/meeting-notes-2026-10-23.md) |
| Current-state process map | Reviewed draft v0.1 | [View diagram](docs/process-analysis/ShopStack-Current-State-Improved.png) · [Open in diagrams.net](https://app.diagrams.net/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fkkrishnan937%2Fshopstack-ba-portfolio%2Fmain%2Fdocs%2Fprocess-analysis%2FShopStack-Current-State-Improved.drawio) · [Download source](https://raw.githubusercontent.com/kkrishnan937/shopstack-ba-portfolio/main/docs/process-analysis/ShopStack-Current-State-Improved.drawio) |
| Gap register | Draft v0.1 | [Read gap register](docs/process-analysis/gap-register.md) |
| Prioritization and decision record | Working priorities; first increment recorded | [Read decision record](docs/process-analysis/prioritization-and-decisions.md) |
| Future-state cart process | Draft v0.3 reconciled with requirements and diagram v0.4 | [Read future-state process](docs/process-analysis/future-state-cart-process.md) |
| Future-state cart diagrams | Draft v0.4; five pages; editor review pending | [View diagrams](docs/process-analysis/future-state-diagrams.md) · [Open in diagrams.net](https://app.diagrams.net/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fkkrishnan937%2Fshopstack-ba-portfolio%2Fmain%2Fdocs%2Fprocess-analysis%2FShopStack-Future-State-Cart-Reviewed.drawio) |
| Future-state walkthrough | Review record v0.1 | [Read walkthrough](docs/process-analysis/future-state-walkthrough.md) |
| Cart recovery workshop | Simulated findings; open recovery questions | [Read workshop notes](docs/discovery/cart-recovery-workshop-2026-10-25.md) |
| Stakeholder analysis and engagement plan | Draft v0.2; simulated review and change control recorded; customer validation pending | [Read stakeholder plan](docs/discovery/stakeholder-analysis-and-engagement.md) |
| Cart requirements, business rules, and acceptance criteria | Draft v0.4; 37 existing criteria; new readiness constraints require expansion | [Read requirements](docs/requirements/cart-requirements.md) |
| Readiness changes and implementation handoff | CR-CART-01; direct author decisions, scope impact and simulated targets | [Read change and handoff](docs/requirements/cart-readiness-change-and-handoff.md) |
| Cart-read information contract | Draft v0.1; five response situations; exact schema/version semantics open | [Read contract](docs/requirements/cart-read-contract.md) |
| Cart wireframes | Draft v0.3; seven illustrative states including expiry and price changes; customer/UX review pending | [Review wireframes](docs/wireframes/cart-wireframes.md) |
| Cart requirements traceability | 37 families mapped; 9 local Pass, 28 Not run | [Read traceability matrix](docs/requirements/cart-traceability-matrix.md) |
| Cart-loading test readiness | Actual frontend inspection; application scenario blocked before execution | [Read readiness record](docs/testing/cart-loading-readiness-2026-10-28.md) |
| Cart delivery-readiness actions | Actual blocker linked; ownership and dates remain simulated/unconfirmed | [Read handoff action log](docs/testing/cart-delivery-readiness-actions.md) |
| Cart-viewing delivery workshop | Simulated slice planning; expiry-message persistence and API design proposed | [Read workshop findings](docs/discovery/cart-viewing-delivery-workshop.md) |
| Defect-lifecycle training example | Hypothetical quantity mismatch; no observed defect or retest | [Read training example](docs/testing/hypothetical-quantity-defect-exercise.md) |
| Detailed quantity-update UAT case | Draft v0.2; partial-result/access rules included; execution Not run | [Read UAT case](docs/testing/quantity-update-uat-case.md) |
| Cart UAT test pack | 37 families; 9 executed locally with results | [Read UAT pack](docs/testing/cart-uat-pack.md) |
| Executed cart-viewing slice | Actual results, screenshots, snapshots and build fingerprint; no independent sign-off | [Read execution record](docs/testing/cart-view-executed-2026-10-28.md) |
| One-page case study | Delivered slice, observed results, limitations and supporting links | [Read case study](docs/case-study.md) |

## Approach

1. Clarify the business request and confirm discovery findings.
2. Map the existing journey and distinguish observed gaps from hypotheses.
3. Evaluate options and define the proposed future process.
4. Document and prioritize requirements with measurable acceptance criteria.
5. Support solution design and delivery, tracing changes to business needs.
6. Execute acceptance scenarios and record actual results and defects.
7. Evaluate outcomes and document lessons and limitations.

## How to review this project

Start with the case study and actual execution record, then follow the linked requirements and analysis. Application source belongs in the ShopStack application repository; this portfolio holds analysis and execution evidence rather than duplicate implementation scripts.

## Updating this repository

- Add artifacts as the work is completed; keep planned work marked as planned.
- Use descriptive commits explaining the document or decision changed.
- Keep artifacts in folders under `docs/`, and update the artifact table when adding a deliverable.
- Record significant scope changes and their rationale rather than silently rewriting prior decisions.
- Distinguish observations, assumptions, proposals, simulated decisions, and executed test results.
- Use synthetic examples and exclude credentials, private customer information, and unsupported outcome claims.

## Current next step

Review the implemented read-only slice and evidence, seek independent feedback, and verify the normal PostgreSQL deployment before a release claim. Close session-reconciliation/logout/retention-contract gates before shipping mutations. The remaining 28 test families and wider checkout are incomplete. Extend the verified path rather than adding further unexecuted drafts.
