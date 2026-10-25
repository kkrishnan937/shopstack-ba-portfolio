# Cart recovery requirements workshop

**Date:** 25 October 2026  
**Status:** Simulated workshop findings; draft requirements review  
**Participants:** Portfolio author practising the BA role; AI-simulated developer, tester, and product owner

## Purpose and evidence boundary

Clarify how quantity updates and removal interact when an earlier update has no confirmed outcome. These notes summarize the voice practice session. They are not actual developer findings, verified application behaviour, independent stakeholder approval, implementation evidence, or UAT results. No delivery estimates or technical investigations were performed during this session.

Related references: [future-state process](../process-analysis/future-state-cart-process.md), especially FS-Q-02; [process walkthrough](../process-analysis/future-state-walkthrough.md); [decision record](../process-analysis/prioritization-and-decisions.md).

## Questions elicited by the BA

- If a quantity update is pending, what could go wrong if the customer removes the same item?
- How should the system prevent an update and removal from conflicting?
- Does pending mean confirmed processing or an unknown outcome, and which states should block removal?
- Does the product owner accept the proposed restriction, and what should the customer be told?
- What must the message explain about why removal is unavailable and what the customer can do next?

## Clarified terminology

| Term | Meaning for the proposed requirements |
|---|---|
| Processing | The system has evidence that the original update is still running. |
| Outcome unknown | No final result is available; the update may have succeeded, failed, or still be running. |
| Loading indicator | A presentation state that does not independently prove either request status. Loading cart contents and submitting an update are separate operations. |

## Risk discussed

If removal completes before an earlier quantity update, the later update could conflict with the removal. Depending on implementation, it might fail, recreate an item, or generate misleading feedback. These are hypothetical risks requiring technical investigation, not observed defects. Retrieving cart contents alone does not prove that an earlier request can no longer alter them.

## Simulated decision and proposed behaviour

The simulated developer recommended blocking removal of the same item while its earlier quantity update is processing or unconfirmed. The simulated product owner accepted that restriction provided the explanation is clear and gives a next action.

- Block removal of the affected item in both states until the earlier request is resolved and can no longer change the cart.
- Explain the restriction without asserting an unverified outcome.
- Offer **Check update status**, which checks the original request without submitting another update or removal.
- If the status check fails, keep the outcome unconfirmed; do not treat a timeout alone as proof of failure or safe completion.
- Do not assume this restriction applies to all cart items; wider interaction rules remain to be reviewed.

Candidate message discussed:

> We haven't confirmed your earlier quantity update yet. Removal is temporarily unavailable. Select "Check update status" to check again.

This wording is a draft for the unconfirmed-outcome case. Wording for a confirmed processing state still requires review. Request-status tracking is a proposed capability, not an existing verified feature.

## Open requirements and technical review actions

| ID | Open item | Proposed review roles | Status |
|---|---|---|---|
| CR-01 | Determine how request status and safe resolution can be established reliably, including concurrent update/removal behaviour. | Developer and technical lead | Open; no actual investigation assigned or completed |
| CR-02 | Define recovery when status remains unconfirmed for a prolonged period, including escalation and safe restoration of editing. Do not invent an automatic unlock timeout. | Product owner with developer/tester input | Open |
| CR-03 | Confirm behaviour of other cart actions while one item's update is unresolved. | Product owner, developer, tester | Open |
| CR-04 | Review accessible status feedback, blocked-control explanation, and wording for each verified state. | Product owner, UX/content, tester | Open |
| CR-05 | Draft and review Given/When/Then criteria for blocked removal, status checks, confirmed resolution, and repeated status-check failure. | BA with developer/tester review | Next exercise; not yet completed |

## Next step

Draft the blocked-removal acceptance criterion, review the open recovery questions, and reconcile the resulting rules with FS-Q-02 and the future-state diagrams. Implementation and test execution remain pending.
