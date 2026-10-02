# Bounded validation and lifecycle acceptance

## Choose correctness checks

Inspect command definitions and hooks. Use at most one applicable build/compile/type/correctness static check and up to three directly affected smoke scenarios. These are optional ceilings, not a requirement to invent tests. A build that already type-checks needs no duplicate type check. A single command that runs a broad suite, audit, vulnerability scan, or deployment is not preliminary validation.

Low generates no unnecessary frontend comments and starts no security checks. Disable generates no unnecessary comments anywhere and starts no defensive pre-delivery work, including security tests, audits, stress tests, broad regression, and unsolicited edge-case campaigns. Do not run those checks under another label. A required quality gate remains required; identify its source and run only that scope.

Repair introduced defects locally and rerun the affected failed check. Report unrelated pre-existing failures without launching a cleanup campaign. Delegation shares the same task budget. Avoid tests that merely repeat the implementation or verify arbitrary wording.

## Explicit authorization

“Run the full regression suite” authorizes that suite for the current task. “Security-test the new login endpoint” authorizes that endpoint's security tests, not a product-wide audit. “Test login and reset on Chrome and Safari” authorizes those named flows and browsers. An explicit scope request overrides the default automatic-check prohibition only for that task and scope.

Continue, finish it, check it, make it robust, and switching engineering mode do not grant broad or security-test authorization. Never persist one-time authorization. A testing request does not authorize deployment, deletion, or unrelated implementation.

## Lifecycle closure acceptance

Check the add/update/remove prompt cycle. Verify within the skill's workflow, using an isolated fixture when testing the skill itself:

- Add the prompt, change modes, then deactivate; the marked prompt block must be absent, with all unrelated document content unchanged. No baseline is saved or restored.
- Verify unrelated edits survive prompt removal; keep the .md file even if empty. Removing an older marked policy must work without snapshot history.
- Check every user-facing message in enable/disable/re-enable or mode-only turns for absence of state indicators. The lifecycle exception covers progress and final text, including a turn that also implements a feature. Do not emit an indicator in order to demonstrate that it is suppressed.
- Keep this acceptance result in the skill workflow or its isolated evaluation evidence. Do not add target-project comments, notes, markers, or transcripts to satisfy the output requirement.

A file-helper test validates prompt removal; it does not prove that a model always follows the output rule. Report that distinction accurately.

## Deliver evidence once

For implementation deliveries, briefly name checks actually run and their result; mention broader checks not run once. Failures and environment blockers must be stated accurately. Pure lifecycle/mode operations need a brief action acknowledgement without a status indicator or validation reminder. For example, after verified prompt removal: “已移除添加的提示词。”
