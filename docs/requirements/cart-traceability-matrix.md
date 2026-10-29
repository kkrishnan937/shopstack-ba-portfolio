# Cart requirements traceability matrix

**Version:** 0.1  
**Date:** 28 October 2026  
**Status:** Draft coverage review; CART-T-04/05 blocked at readiness, other outlines Not run
**Prepared by:** Kailas Krishnan

## Scope and interpretation

Maps the first increment's seven functional requirements and 37 acceptance criteria to business sources, draft designs and planned test outlines. Sources are [requirements v0.3](cart-requirements.md), the [gap register](../process-analysis/gap-register.md), [decision record](../process-analysis/prioritization-and-decisions.md) and [wireframes v0.3](../wireframes/cart-wireframes.md). These are portfolio case-study artifacts; simulated decisions do not establish actual stakeholder approval.

Each CART-T identifier below reserves a planned test outline, not an executed test or a complete UAT script. CART-T-04 and CART-T-05 are **Blocked** after the [28 October readiness check](../testing/cart-loading-readiness-2026-10-28.md). Other outlines remain **Not run**. No outlined application acceptance scenario has completed execution; readiness observations and build evidence are recorded separately. Prototype checks reported in the wireframe notes do not count as application UAT. Parameterized outlines must be expanded into separately recorded cases in the detailed test plan.

Design coverage means that an illustrative screen exists. It does not prove implemented behaviour, backend consistency, feasibility, usability or accessibility. A mapped criterion is not necessarily ready for delivery. Open requirements and missing designs are tracked below; they are not silently counted as complete.

## Requirement and business-source map

| Requirement / story | Business source and purpose | Related rules / decisions | Criterion IDs | Review limitations |
|---|---|---|---|---|
| CART-FR-01 / US-01: Review cart | GAP-02: customers cannot verify selections or subtotal through the existing interface | CART-BR-03; DEC-05 | CART-AC-01 through CART-AC-07 | Multi-item and actual navigation/integration coverage exceed the single-item preview |
| CART-FR-02 / US-02: Update quantity | GAP-03: customers cannot correct quantities through the existing interface | CART-BR-01 through CART-BR-06; DEC-04 | CART-AC-08 through CART-AC-20; CART-AC-33 through CART-AC-34 | Status tracking and prolonged recovery unresolved; retention also traces to CART-FR-06 |
| CART-FR-03 / US-03: Remove line | GAP-03: customers cannot remove unwanted selections | CART-BR-02, CART-BR-04 through CART-BR-06 | CART-AC-21 through CART-AC-23; shared CART-AC-13 | Unknown-removal recovery and concurrent actions require review |
| CART-FR-04 / US-04: Log out | GAP-05 and DEC-06: customers need to end signed-in access | CART-BR-08; DEC-06 | CART-AC-24 and CART-AC-32 | Success guarantee, revocation and failures unresolved; no logout design |
| CART-FR-05 / US-05: Merge additions | DEC-03 and DEC-04 refine the cart-review/management need; not a separately observed customer finding | CART-BR-01; DEC-03, DEC-04 | CART-AC-25 through CART-AC-27 | Catalog addition and multi-variant interaction not designed |
| CART-FR-06 / US-06: Retain/expire cart | DEC-02 and DEC-08 define simulated retention policy; no observed demand or regulatory requirement claimed | CART-BR-08; DEC-02, DEC-08 | CART-AC-28 through CART-AC-29 and CART-AC-32 through CART-AC-36 | Real clock, persistence and in-flight expiry behaviour unverified |
| CART-FR-07 / US-07: Price changes | DEC-09 refines transparent cart pricing in GAP-02 | CART-BR-03; DEC-09 | CART-AC-30 through CART-AC-31 and CART-AC-37 | DG-01 proposed designs prepared; stakeholder/customer review pending |

The CART-FR-07 register row in requirements v0.3 still says policy approval is pending, while its US-07 section and DEC-09 record confirmation within the simulation. Use the latter to interpret the case-study policy, and reconcile the stale register label in the next requirements revision. No independent approval is implied.

## Design references

| Code | Draft design | Coverage boundary |
|---|---|---|
| WF-N | [Normal cart](../wireframes/cart-normal.png) | One mug line; local quantity and removal demonstrations |
| WF-E | [Empty cart](../wireframes/cart-empty.png) | Confirmed empty result and next action |
| WF-X | [Expired cart](../wireframes/cart-expired.png) | Expiry explanation only; no real retention engine |
| WF-L | [Loading failure](../wireframes/cart-error.png) | Initial-load error without confirmed contents/subtotal |
| WF-U | [Unconfirmed update](../wireframes/cart-unknown.png) | Last-confirmed values and blocked affected-item actions; not every recovery branch |
| WF-P+ | [Price increase](../wireframes/cart-increase.png) | Old/new unit-price notice and recalculated single-line totals |
| WF-P- | [Price decrease](../wireframes/cart-decrease.png) | Old/new unit-price notice and recalculated single-line totals |
| Missing | No dedicated reviewed design | A related normal/error screen is not a substitute for the missing state |

## Acceptance criteria to planned tests

The test status column describes application execution only. All expected outcomes below are proposals copied or summarized from the criteria, not actual results. See BLK-CART-01 in the readiness record for blocked prerequisites.

| Criterion | Requirement | Design coverage | Planned test / expected verification | Execution |
|---|---|---|---|---|
| CART-AC-01 | CART-FR-01 | WF-N; illustrative | CART-T-01: Compare displayed product name, quantity, unit price, line total and CAD subtotal with owned saved-cart data. | Not run |
| CART-AC-02 | CART-FR-01 | WF-N partial; multi-item layout missing | CART-T-02: Two mugs at CAD 12.50 plus one mouse at CAD 24.99 yield line totals CAD 25.00 / CAD 24.99 and subtotal CAD 49.99. | Not run |
| CART-AC-03 | CART-FR-01 | WF-E | CART-T-03: Successful empty retrieval shows Cart is empty, CAD 0.00 and Continue shopping. | Not run |
| CART-AC-04 | CART-FR-01 | WF-L | CART-T-04: Failed retrieval shows error and Retry; no confirmed empty-cart claim or zero subtotal. | Blocked: BLK-CART-01 |
| CART-AC-05 | CART-FR-01 | WF-L; retrieval integration absent | CART-T-05: Retry retrieves saved state without adding, updating or removing items. | Blocked: BLK-CART-01 |
| CART-AC-06 | CART-FR-01 | WF-N / WF-E; product destination not designed | CART-T-06: Continue shopping returns to browsing with saved data unchanged; execute from empty and non-empty carts separately. | Not run |
| CART-AC-07 | CART-FR-01 | All seven states | CART-T-07: Verify demo tax/shipping/payment notice wherever the cart is displayed. | Not run |
| CART-AC-08 | CART-FR-02 | WF-N local interaction; persisted save absent | CART-T-08: Change two mugs to ten; confirm quantity 10, line/subtotal CAD 125.00 and success message. | Not run |
| CART-AC-09 | CART-FR-02 | WF-N local interaction; persisted save absent | CART-T-09: Change two mugs to one; confirm quantity 1, line/subtotal CAD 12.50 and success message. | Not run |
| CART-AC-10 | CART-FR-02 | WF-N local validation; dedicated error capture missing | CART-T-10: Separately reject 0, -1, 1.5, text, blank and 11 with the agreed message and no saved quantity/total changes. | Not run |
| CART-AC-11 | CART-FR-02 | WF-N partial; multi-item state missing | CART-T-11: Change mugs from two to three while keeping one mouse; mug line CAD 37.50 and subtotal CAD 62.49. | Not run |
| CART-AC-12 | CART-FR-02 | Missing confirmed-save-failure state | CART-T-12: Confirmed failure preserves two mugs and CAD 25.00; show failure message, allow customer retry, no automatic repeat. | Not run |
| CART-AC-13 | CART-FR-02 / CART-FR-03 | WF-U | CART-T-13: An unconfirmed earlier update prevents removal of that item, explains restriction and offers Check update status. | Not run |
| CART-AC-14 | CART-FR-02 | WF-U; tracking integration absent | CART-T-14: Status action checks the original request without another update or removal; verify request identity and mutation count. | Not run |
| CART-AC-15 | CART-FR-02 | Missing terminal-success recovery state | CART-T-15: Terminal success plus fresh quantity 3 shows CAD 37.50 totals and Update confirmed; safe resolution permits removal without repeated update. | Not run |
| CART-AC-16 | CART-FR-02 | Missing success-confirmed/refresh-failed state | CART-T-16: Confirmed update plus failed retrieval shows accurate explanation, last-confirmed values, blocked removal and Refresh cart. | Not run |
| CART-AC-17 | CART-FR-02 / CART-FR-03 | WF-N result only; recovery transition missing | CART-T-17: Successful refresh after CART-T-16 displays saved values and enables removal if the item remains; no repeated update. | Not run |
| CART-AC-18 | CART-FR-02 / CART-FR-03 | Missing terminal-failure recovery state | CART-T-18: Terminal failure and fresh quantity 2 show CAD 25.00 totals and failure message; enable removal and optional customer retry. | Not run |
| CART-AC-19 | CART-FR-02 | Missing verified-processing state; WF-U is not equivalent | CART-T-19: Verified processing keeps further update/removal blocked for that item and status check available; exact message still needs review. | Not run |
| CART-AC-20 | CART-FR-02 | WF-U local repeated-check feedback | CART-T-20: Failed status check preserves unconfirmed wording, last-confirmed labels and restrictions; offer another status check, not automatic mutation. | Not run |
| CART-AC-21 | CART-FR-03 | WF-N partial; remaining-mouse state missing | CART-T-21: Remove the two-mug line while one mouse remains; show only mouse and CAD 24.99 totals with success notice. | Not run |
| CART-AC-22 | CART-FR-03 | WF-N to WF-E local transition | CART-T-22: Remove the only product line; show Cart is empty, CAD 0.00 and Continue shopping. | Not run |
| CART-AC-23 | CART-FR-03 | Missing confirmed-removal-failure state | CART-T-23: Confirmed failed removal preserves both mugs and CAD 25.00; failure notice and customer-controlled retry. | Not run |
| CART-AC-24 | CART-FR-04 | Missing logout design; security scope open | CART-T-24: Once the logout guarantee is agreed, verify it, preserved cart/expiry and reauthentication for protected changes. | Not run |
| CART-AC-25 | CART-FR-05 | WF-N result concept only; addition interaction missing | CART-T-25: Add one identical product/variant to two mugs; exactly one line, quantity 3, unit CAD 12.50 and line CAD 37.50. | Not run |
| CART-AC-26 | CART-FR-05 | Missing merged-limit rejection state | CART-T-26: Add one identical mug to ten; reject, preserve ten and totals, show per-product/variant limit message. | Not run |
| CART-AC-27 | CART-FR-05 | Missing multi-variant state | CART-T-27: Add one red mug to two blue mugs; display separate variant lines with quantities 1 and 2. | Not run |
| CART-AC-28 | CART-FR-06 | WF-X; no real expiry implementation | CART-T-28: Retrieve after elapsed retention; no expired items, expiry explanation, CAD 0.00 and Continue shopping. | Not run |
| CART-AC-29 | CART-FR-06 | WF-N result only; persistence not represented | CART-T-29: Retrieve 20 days after last change; saved items remain and sign-in/viewing leave original expiry unchanged. | Not run |
| CART-AC-30 | CART-FR-07 | WF-P+; DG-01 review pending | CART-T-30: Two mugs increase from CAD 12.50 to CAD 14.00; affected-line text shows old/new prices and line/subtotal CAD 28.00 without colour dependence. | Not run |
| CART-AC-31 | CART-FR-07 | Missing stale-price refresh-failure state; WF-L lacks retained values | CART-T-31: Failed price refresh never confirms a new price; retained values last confirmed, accurate error and Refresh cart. | Not run |
| CART-AC-32 | CART-FR-04 / CART-FR-06 | Missing logout interaction; retention backend-only aspect | CART-T-32: Logout at day 20 preserves original expiry and ten days remaining; security guarantee requires separate resolution. | Not run |
| CART-AC-33 | CART-FR-02 / CART-FR-06 | WF-N update concept only; no clock implementation | CART-T-33: Successful quantity change at T resets expiry to T plus 30 times 24 hours. | Not run |
| CART-AC-34 | CART-FR-02 / CART-FR-06 | Missing confirmed-failure state; clock not represented | CART-T-34: Confirmed failed update at day 20 does not reset expiry; ten days remain. | Not run |
| CART-AC-35 | CART-FR-06 | WF-N result only; clock boundary not represented | CART-T-35: At one second before expiry, successful retrieval returns active items and does not reset the clock. | Not run |
| CART-AC-36 | CART-FR-06 | WF-X result only; clock boundary not represented | CART-T-36: Execute exact-expiry and after-expiry cases separately; exclude expired items, explain expiry, CAD 0.00 and Continue shopping. | Not run |
| CART-AC-37 | CART-FR-07 | WF-P-; DG-01 review pending | CART-T-37: Two mugs decrease from CAD 14.00 to CAD 12.50; affected-line notice and line/subtotal CAD 25.00 without colour dependence. | Not run |

## Detailed test scripts

[CART-UAT-01: Successful quantity update](../testing/quantity-update-uat-case.md) expands CART-T-11 using its two-mug/one-mouse fixture. The [cart UAT pack](../testing/cart-uat-pack.md) expands the other 36 outlines with setup, procedures, expected results and blank execution fields. Supporting persistence checks and technical test methods require review. Existing execution statuses remain unchanged: no completed application acceptance scenarios or new readiness checks are claimed.

## Open decisions and coverage actions

| Reference | Impact | Proposed next action / review roles |
|---|---|---|
| CART-Q-01 through CART-Q-03 | Recovery tests can describe defined branches but cannot establish complete safe recovery or release readiness. | Product owner, technical lead and tester review terminal guarantees, prolonged unknown outcomes, failure/retrieval conflicts and concurrency. |
| CART-Q-04 | Session-expiry scenarios lack complete agreed expected outcomes and corresponding test outlines. | Define them with business/development/testing input before adding tests; these are additional to the 37 mapped criteria. |
| CART-Q-05 | Native controls and local checks do not establish accessibility or usability acceptance. | Plan keyboard, focus, status-announcement and representative-customer reviews; do not infer compliance. |
| CART-Q-06 | Unknown removal outcomes, retention/in-flight interactions and additional reset cases remain open. | Define missing criteria; add separate successful-addition/removal reset tests based on DEC-08, and review expiry message persistence. |
| CART-Q-07 | Artifacts must remain consistent as requirements change. | Maintain this matrix with versioned process, design and test updates; native diagram-editor verification remains pending. |
| CART-Q-08 | Successful logout and failure behaviour cannot be fully tested until scope is agreed. | Investigate token invalidation; product owner records scoped guarantee before baselining affected criteria. |
| DG-01 | Price-notice designs exist, but no stakeholder/customer validation has closed the design gap. | Review WF-P+ and WF-P- with proposed UX, product owner, developer and tester roles; dates and actual participants remain unassigned. |
| Additional design coverage | Multi-item, variant, confirmed-failure, processing and recovery-completion states are not fully depicted. | Prioritize required states for design review; keep partial mappings explicit. |

All role assignments above are proposed or simulated. They do not establish real staff commitments. GAP-01 registration and GAP-04 demo orders remain in the wider release and outside this first-increment matrix. A seven-state wireframe does not provide complete visual coverage of all seven stories.

## Coverage summary and next step

- All seven CART-FR requirements have a business-source mapping.
- All 37 existing CART-AC criteria have a mapped test outline; shared requirements are explicitly identified.
- There are 37 planned test outlines, not 37 executed or passing tests. Parameter expansion will produce additional cases.
- CART-T-04 and CART-T-05 are Blocked at readiness; the remaining 35 outlines are Not run. The readiness record is not completed application acceptance evidence. No baseline approval or release decision is recorded.
- Missing criteria and designs remain visible; mapping completeness is not functional completeness.

Next, review mappings with the proposed business/development/testing roles, then expand test outlines into detailed scripts with preconditions, synthetic data, steps, expected outcomes, environment/build, actual results, evidence and defect/retest references. Leave results blank until actual execution.
