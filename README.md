# ShopStack Business Analyst Portfolio

*This project follows a simulated business analysis process.*

**Customer Purchase Journey Improvement**  
**Author:** Kailas Krishnan  
**Status:** In progress: future-state process definition

An independent Business Analyst case study using an existing e-commerce learning application to practise an end-to-end business analysis workflow. This repository will grow as discovery, process analysis, requirements, validation, and evaluation work is completed and reviewed.

## Business context

[ShopStack](https://github.com/kkrishnan937/shopstack) is an e-commerce application. Its customer interface displays products and supports login and add-to-cart requests, but has no visible cart review or order submission journey.

This case study investigates how customers could review their selections and submit a demo order. Customer abandonment, conversion impact, and financial benefits have not been measured.

## Proposed outcome and scope

Enable customers to register or log in, add products, review cart items and totals, update quantities, remove items, and submit a demo order with confirmation. Display prices explicitly in CAD.

The simulated sponsor retained authentication before adding items. Guest cart and guest checkout are future proposals, not agreed release scope.

Real payments and shipping/fulfilment are excluded. Demo orders must clearly state that no payment was taken and no shipping is arranged. Tax treatment, total calculation rules, measurement definitions, and inventory scope remain open questions.

## Portfolio artifacts

| Artifact | Status | Link |
|---|---|---|
| Discovery meeting notes | Draft for simulated sponsor confirmation | [Read meeting notes](docs/discovery/meeting-notes-2026-10-23.md) |
| Current-state process map | Reviewed draft v0.1 | [View diagram](docs/process-analysis/ShopStack-Current-State-Improved.png) · [Open in diagrams.net](https://app.diagrams.net/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fkkrishnan937%2Fshopstack-ba-portfolio%2Fmain%2Fdocs%2Fprocess-analysis%2FShopStack-Current-State-Improved.drawio) · [Download source](https://raw.githubusercontent.com/kkrishnan937/shopstack-ba-portfolio/main/docs/process-analysis/ShopStack-Current-State-Improved.drawio) |
| Gap register | Draft v0.1 | [Read gap register](docs/process-analysis/gap-register.md) |
| Prioritization and decision record | Working priorities; first increment recorded | [Read decision record](docs/process-analysis/prioritization-and-decisions.md) |
| Future-state cart process | Proposed draft v0.2 | [Read future-state process](docs/process-analysis/future-state-cart-process.md) |
| Future-state cart diagrams | Draft v0.3; three pages | [View diagrams](docs/process-analysis/future-state-diagrams.md) · [Open in diagrams.net](https://app.diagrams.net/#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fkkrishnan937%2Fshopstack-ba-portfolio%2Fmain%2Fdocs%2Fprocess-analysis%2FShopStack-Future-State-Cart-Reviewed.drawio) |
| Future-state walkthrough | Review record v0.1 | [Read walkthrough](docs/process-analysis/future-state-walkthrough.md) |
| Cart recovery workshop | Simulated findings; open recovery questions | [Read workshop notes](docs/discovery/cart-recovery-workshop-2026-10-25.md) |
| Stakeholder analysis and engagement plan | Draft v0.2; simulated review and change control recorded; customer validation pending | [Read stakeholder plan](docs/discovery/stakeholder-analysis-and-engagement.md) |
| Cart requirements, business rules, and acceptance criteria | Draft v0.3; 37 criteria; retention/price rules clarified; recovery and logout scope open | [Read requirements](docs/requirements/cart-requirements.md) |
| Wireframes and requirements traceability | Planned | Not yet created |
| UAT scenarios, execution evidence, and defect log | Planned | Not yet created |
| Solution evaluation and final case study | Planned | Not yet created |

## Approach

1. Clarify the business request and confirm discovery findings.
2. Map the existing journey and distinguish observed gaps from hypotheses.
3. Evaluate options and define the proposed future process.
4. Document and prioritize requirements with measurable acceptance criteria.
5. Support solution design and delivery, tracing changes to business needs.
6. Execute acceptance scenarios and record actual results and defects.
7. Evaluate outcomes and document lessons and limitations.

## How to review this project

Start with the discovery notes. Follow later artifacts through the table above as they are added. The application source remains in the original ShopStack repository; this repository contains BA deliverables rather than a duplicate application.

## Updating this repository

- Add artifacts as the work is completed; keep planned work marked as planned.
- Use descriptive commits explaining the document or decision changed.
- Keep artifacts in folders under `docs/`, and update the artifact table when adding a deliverable.
- Record significant scope changes and their rationale rather than silently rewriting prior decisions.
- Distinguish observations, assumptions, proposals, simulated decisions, and executed test results.
- Use synthetic examples and exclude credentials, private customer information, and unsupported outcome claims.

## Current next step

Consolidate the reviewed cart recovery behaviour and recorded decisions into the future-state process, then develop requirements and acceptance criteria. Decisions recorded on 25 October include 30-day cart retention, identical-variant merging, a 10-unit limit per product/variant, item-price subtotals without tax/shipping calculations, logout in the first increment, and exclusion of stock checks and inventory reservation. Implementation and UAT remain pending.
