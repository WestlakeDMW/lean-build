---
name: lean-build
description: Control optional defensive engineering and test scope when the user asks for lean implementation, less overengineering, or a Defensive Construction mode.
---

# lean-build

Complete the requested work with only the engineering its actual requirements need.

## 1. Lifecycle and mode

Skill activation is separate from the engineering mode. Enabling the skill applies a reversible project policy; disabling the skill removes that overlay and restores the settings that existed before activation. `Disable` is an engineering mode while the skill remains active, not a request to turn the skill off.

Resolve the target project root from the user's project context or repository root, never from the skill installation directory. Read its `Soul.md` before editing. Before the first persistent activation, capture the original managed block, file existence, and session preferences changed by this skill. Keep the baseline across mode changes and repeated activation. Restore the prior overlay to that baseline before applying a fresh overlay; do not replace the baseline with the skill's own settings. On deactivation, restore the baseline immediately, clear temporary overrides and skill-specific session preferences, and stop applying this policy. Do not uninstall the skill or reset unrelated user settings.

Use the latest explicit mode instruction still applicable to this project and scope, then an active temporary override, then the valid stored mode, then Low. Ignore expired instructions. Valid modes are Enable, Low, and Disable. Persist activation and mode changes by default; preserve a valid stored mode on reinvocation without a new selection. Temporary/task-only/session-only requests and status queries do not write files. Unqualified temporary requests are task-only; they expire after final delivery. Session-only overrides expire at session end. Restore the preceding session state on expiry; any later explicit mode instruction replaces the override. Never persist test authorization.

If the project root is unclear, files are inaccessible, or a legacy activation has no recorded baseline, report what could not be saved or restored. Do not invent previous settings or claim restoration without evidence. Preserve unrelated edits made while the skill was active.

## 2. Engineering levels

| Mode | Comments and construction | Automatic checks |
| --- | --- | --- |
| Enable | Proportionate handling for concrete relevant failures; useful concise explanations. No speculative future requirements. | Preliminary correctness checks only; no automatic security testing. |
| Low | Default. Generate no unnecessary frontend comments, including component/CSS headings, obvious explanations, redundant type narration, or speculative TODOs. No optional fallback layers, frameworks, or future extension points. | No proactively initiated security checks, audits, vulnerability/dependency scans, or hardening verification. Preliminary correctness checks remain available. |
| Disable | Generate no unnecessary comments in any code. No optional defensive handling, compatibility layers, hardening, or speculative extensions. | No proactive pre-delivery defensive construction or checks, including security tests, audits, stress tests, broad regression, or edge-case campaigns. Preliminary correctness checks remain available. |

These prohibitions apply to all possible discretionary additions within the task, not only a list of examples. Do not relabel a security check as a smoke or static check to run it. A fresh explicit user request for a particular security test or other broader check authorizes only that named scope for the current task; it does not re-enable automatic checks.

Complete the requested behavior in every mode. Keep necessary correctness, actual platform/API contracts, required license notices and tool directives, and comments explaining constraints that would otherwise invite an incorrect change. Do not use this skill to delete existing comments or protections, disable product security functionality, or waive required quality gates or higher-priority instructions. If a required gate conflicts with the optional-check limit, name its concrete source and perform only the required scope.

Before discretionary work, identify its present requirement or concrete relevant failure. If neither exists, omit it. Fix defects introduced by your changes without starting unrelated refactors, retry/logging infrastructure, backend redesign, or repository-wide cleanup.

## 3. Validation authorization

By default, choose at most one relevant build, compile, type, or correctness-focused static check, up to three bounded smoke scenarios, and a brief diff review. These are ceilings, not a checklist. Inspect command definitions and lifecycle hooks; judge actual coverage and effects rather than command count. Avoid equivalent successful checks, all-page/device/browser sweeps, and scripts that bundle broader testing, security scans, or deployment. After a local fix, rerun only the affected failed check.

Full functional testing, comprehensive regression, security testing/audits, broad end-to-end testing, and stress testing require an explicit user request specifying the scope. Concrete requests to test named flows authorize those flows. Authorization applies only to this task and scope; never store it as a default. Continue, finish it, check it, make it more robust, and switching to Enable do not authorize broad or security testing. Disable does not stop preliminary correctness checks. Delegation does not multiply the task's validation allowance.

At a delivery after implementation or modification, briefly report once the checks actually run and their outcomes, and broader testing not run. Report failures, unrun checks, and environment blockers accurately; never claim full validation from a build. Do not repeat this reminder during planning, progress, pure discussion, status queries, or lifecycle/mode-only operations.

## 4. User-facing output

For any turn that enables, disables, re-enables, or only changes the skill mode, do not output any state indicator in any user-facing message, including progress and final replies. Suppress banners, mode badges, and equivalent enabled/disabled or mode announcements for the entire turn, even if it also contains implementation work. Acknowledge the completed action briefly, without a status label. This exception takes precedence over the ordinary active-work rule below.

For ordinary implementation turns while the skill is already active, start each user-facing text message with one English line using the effective mode, for example `Defensive Construction: Low`. Keep the rest in the user's preferred language. After deactivation, stop adding this line.

Never place status indicators, lifecycle acceptance notes, or acceptance transcripts in target-project files, source comments, application UI, generated artifacts, or tool argument text. Required mode parameters and the internal Mode field in the managed policy are operational data, not output indicators. Verify lifecycle output suppression within the skill workflow itself; do not add project remarks as a substitute for that acceptance check.

## 5. Project persistence and restoration

Manage only the defensive-construction block in project-root Soul.md. Keep complete English rules, preserve content outside the block, and read back after writes. Store the pre-activation baseline outside the target project, keyed by its resolved root. Never record only a default mode as a substitute for the actual prior settings.

On deactivation, restore the previous managed block if one existed, otherwise remove the skill-added block. If the skill created Soul.md and nothing unrelated remains, remove the file. Preserve unrelated content added during activation. If the owned block was externally edited or markers are incomplete, reversed, or duplicated, leave it unchanged and report a restoration conflict. Without a baseline, do not guess or silently remove legacy policy.

Do not edit AGENTS.md, global configuration, build scripts, CI, or product settings as part of activation. Soul.md needs an explicitly configured instruction entry point for automatic cross-session loading. Restoration applies to this skill's policy and session settings, not code changes implemented for the user's task.

## Conditional resources

- Read [validation.md](references/validation.md) when selecting checks or verifying lifecycle output.
- Read [persistence.md](references/persistence.md) before activation, policy writes, or restoration.
- Use [update_soul.py](scripts/update_soul.py) for persistent activation/mode changes and deactivation; Python 3 standard library only. Do not run it for temporary modes or status queries.
