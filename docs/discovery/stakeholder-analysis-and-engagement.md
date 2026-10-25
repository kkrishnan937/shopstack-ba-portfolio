# Stakeholder analysis and engagement plan

**Date:** 25 October 2026  
**Version:** 0.1  
**Status:** Draft for simulated role review  
**Prepared by:** Kailas Krishnan, portfolio author practising the BA role

## Purpose and evidence boundary

Identify who is affected by the proposed ShopStack improvements, who contributes evidence, and who makes decisions. This is an independent case study: roles below are simulated or proposed, not recruited participants or a real delivery organization. Influence and interest assessments are initial hypotheses requiring review. No actual stakeholder agreement or acceptance authority is claimed.

The first increment covers existing customers' cart review, management, and logout. Registration and demo orders remain in wider release scope. See the [discovery notes](meeting-notes-2026-10-23.md), [decision record](../process-analysis/prioritization-and-decisions.md), and [recovery workshop](cart-recovery-workshop-2026-10-25.md).

## Stakeholder register

| ID | Role and assignment | Interest / impact | Proposed authority or contribution | Influence / interest | Engagement approach |
|---|---|---|---|---|---|
| ST-01 | Sponsor / product owner; simulated, actual assignment absent | Customer outcomes, bounded scope, priorities and release tradeoffs | Decide business scope, priorities and policy; proposed business acceptance authority, subject to explicit confirmation | High / high | Collaborate on rules and tradeoffs; review decisions and acceptance criteria |
| ST-02 | Existing signed-in customer; representative not recruited | Understand selections and totals, correct items, recover from uncertainty, end session | Provide task and usability evidence; not responsible for technical design | Low formal authority / high | Observe tasks and review prototypes; include differing access needs |
| ST-03 | Prospective new customer; representative not recruited | Create an account and complete the wider demo journey | Inform registration and access needs; first increment does not resolve their full journey | Low formal authority / high | Consult during wider-release discovery; explain first-increment limitations |
| ST-04 | Developer / technical lead; simulated, actual assignment absent | Feasibility, data consistency, dependencies and maintainability | Assess options and effort; define technical design and evidence needed for reliable status tracking | High technical influence / high | Joint refinement and technical reviews; investigate unresolved recovery risks |
| ST-05 | Tester / test lead; simulated, actual assignment absent | Clear expected results, realistic test data, coverage and defect evidence | Review testability, plan tests, report actual outcomes and residual risk; business acceptance is a separate decision | Medium / high | Review criteria early; trace scenarios to requirements; review defects and retests |
| ST-06 | UX / content / accessibility contributor; proposed, actual assignment absent | Understandable controls, status messages and accessible interactions | Recommend interaction and content design; validate usability with customer input | Medium / high | Review wireframes, blocked actions, focus behaviour and feedback before implementation |
| ST-07 | Customer support; proposed, actual assignment absent | Explain uncertain outcomes and avoid confusing recovery instructions | Supply support evidence if available; review recovery language and escalation needs | Medium / medium | Targeted exception workshops and message reviews; do not invent support findings |
| ST-08 | Operations / order representative; proposed, actual assignment absent | Understand demo order meaning and retained details | Clarify order lifecycle and confirmation needs for later increments | Medium / medium | Consult before demo-order requirements are baselined; real fulfilment remains excluded |
| ST-09 | Business analyst; portfolio author | Shared understanding, traceable decisions and usable requirements | Facilitate, document, analyse impacts and follow up; do not unilaterally approve business policy or technical estimates | Medium / high | Maintain artifacts, open actions and review records across the lifecycle |

Low formal influence does not imply low importance: customers' needs must be represented even when they cannot approve scope. One person may cover several roles in a small team; decision responsibility should still be explicit.

## Decision and consultation map

These assignments are proposed for the exercise and require review rather than representing an agreed organizational RACI.

| Topic | Proposed decision responsibility | Consult before decision | BA contribution |
|---|---|---|---|
| Quantity limits, retention, pricing policy and release scope | Sponsor / product owner | Customers, developer, tester, relevant specialist | Elicit rationale, document rule and impact, obtain recorded confirmation |
| Request tracking, concurrent changes and migration approach | Developer / technical lead within agreed business constraints | Tester and product owner; specialist if needed | Clarify guarantees, dependencies and unresolved business consequences |
| Error wording and recovery interaction | Product owner for business meaning; UX/content recommends design | Developer, tester, customers, support | Separate verified status from assumptions; record reviewed wording and next actions |
| Testing approach and evidence | Tester / test lead for test planning | Developer, BA and business reviewers | Make expected outcomes measurable and trace tests to requirements |
| Release scope and acceptance of business risk | Sponsor / product owner, authority to be confirmed | Delivery team and business reviewers | Present options, impacts, evidence and unresolved risks; record the decision |
| Business acceptance | Named business acceptance owner, not yet assigned | Customers/reviewers, tester, developer and BA | Support UAT and document whether acceptance is self-review, simulated or independent |

## Engagement plan

| Activity / trigger | Roles to involve | Method | Intended output / evidence |
|---|---|---|---|
| Initiation and material scope change | Product owner, BA, delivery representatives | Scope and objectives discussion | Problem, boundaries, decision authority and assumptions |
| Discovery of customer tasks | Customers, support, product owner, BA | Walkthroughs, interviews or explicitly labelled role-play | Observations distinguished from hypotheses; no invented metrics |
| Story refinement before implementation | Product owner, developer, tester, BA; UX as relevant | Scenario workshop and artifact review | Reviewed stories, rules, acceptance criteria and open actions |
| Unresolved technical recovery or estimate uncertainty | Developer/technical lead, tester, product owner, BA | Focused investigation review | Options, evidence, effort assumptions, risks and decision follow-up |
| Wireframe review | Customers, UX/content, product owner, developer, tester, BA | Task-based prototype walkthrough | Usability findings and changes linked to requirements |
| Delivery question, defect or requested change | Affected roles, with decision owner | Targeted clarification / change review | Updated requirement version, impact and recorded decision |
| Acceptance preparation and execution | Named business reviewers, tester, developer, BA | UAT review and execution | Actual results, defects, retests, limitations and acceptance decision |
| Release forecast changes | Product owner and affected stakeholders | Concise update with assumptions and next check | Clear distinction between forecast and commitment |
| Post-increment evaluation | Product owner, customer/reviewer, delivery team, BA | Evidence review and retrospective | Measured results where available, lessons and remaining work |

Meeting frequency, channels and named contacts are not established. Agree them with participants rather than assume a fixed ceremony schedule. Share relevant pre-reading, invite questions, document disagreements, and confirm owners and dates for follow-up actions.

## Open stakeholder actions

| ID | Action | Proposed lead | Status |
|---|---|---|---|
| SE-01 | Review whether the roles and initial influence/interest assessments are appropriate; identify missing affected groups. | BA with simulated product owner | Open |
| SE-02 | Confirm who can approve scope, business rules and acceptance, and whether sponsor/product owner are separate roles. | Simulated sponsor / product owner | Open |
| SE-03 | Define how customer needs, including accessibility needs, will be represented; obtain permission before using real feedback. | BA | Open |
| SE-04 | Confirm role coverage for UX, support, testing and technical review; record unavailable expertise as a limitation. | Simulated product owner / delivery lead | Open |
| SE-05 | Agree engagement methods, review timing and an escalation route for unresolved decisions. | BA with participating roles | Open |

## Review and maintenance

Review this register when scope, participants, authority or delivery risks change. Keep real engagement evidence separate from simulated practice. This draft does not establish that any planned interviews, technical investigations or UAT sessions have occurred.
