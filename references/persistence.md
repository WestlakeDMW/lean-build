# Project persistence

## Write protocol

1. Resolve the target project root from the active project context or repository root. A user-provided project root takes precedence. Do not use the skill installation root by accident.
2. Read `Soul.md` before editing. Read only the mode inside this skill's managed block; unrelated text or examples do not set the mode. A valid stored mode is exactly `Enable`, `Low`, or `Disable` on one `Mode:` line.
3. For first persistent activation, use `Low` unless the user selected a mode. Preserve a valid stored mode on later activation without a new selection. A temporary/task-only/session-only request and a status query do not write a file. Unqualified temporary requests last through the current task's final delivery; explicit session-only requests last through the session. On expiry, discard the override and restore the stored mode or `Low`.
4. Create or replace only the managed block below, substituting the selected mode. Preserve all existing bytes outside the block, including other policies. If no block exists, append it once with an appropriate line break. Repeated use must not duplicate it.
5. If markers are incomplete, reversed, or duplicated, leave the file unchanged and report that persistence was not completed. Apply the resolved mode in-session. An invalid stored mode is not a saved setting: use `Low` in-session and leave the existing block unchanged unless the user explicitly selects a persistent replacement mode.
6. Read the saved file back. Confirm one complete block, the selected mode, the complete rule body, and unchanged content outside the block. Report success only after this check.

Keep the rules in English. Do not persist transient test permissions or a temporary mode. Do not edit `AGENTS.md`, user-wide instruction files, or global configuration as part of activation.

## Optional helper

The bundled helper uses Python 3 standard-library modules only. After reading the destination and resolving the mode, it can be run as:

```sh
python3 /path/to/lean-build/scripts/update_soul.py --project-root /path/to/project --mode Low
```

The helper never discovers the project root or decides whether a change is authorized; the agent supplies those decisions. It refuses malformed markers, preserves bytes outside the block, and verifies the saved bytes. Do not call it for a temporary mode or status query. If Python is unavailable, follow the same protocol with the available file tools.

## Cross-session entry point

`Soul.md` is a custom policy file. Saving it alone does not ensure a host will load it automatically. If the user explicitly asks to connect cross-session loading, add this line to the project's effective instruction entry point, preserving its existing content:

```text
At the start of each task, read the project-root Soul.md if it exists and apply its Defensive Construction Policy to this project.
```

In Codex this is usually the effective `AGENTS.md`; account for `AGENTS.override.md` and local instruction precedence. Do not silently change the entry point or global configuration. For current discovery behavior, consult the [official AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

## Complete managed block

This is the persistent output template. Keep its behavior aligned with `SKILL.md`. Replace only the `Mode:` value; the template is complete so future sessions do not need the installed skill to interpret it.

```markdown
<!-- defensive-construction:begin -->
## Defensive Construction Policy

Mode: Low

### Scope and state

Apply this policy to the current project. Complete all requested behavior and fix defects introduced by your changes. The policy limits discretionary engineering; it does not reduce feature completeness or necessary correctness. Follow higher-priority instructions and preserve required quality gates. Identify a concrete conflicting requirement and its source rather than silently waiving it.

Use the latest explicit user mode instruction still applicable to this project and scope, then an active temporary override, then the valid stored mode above, then Low. Ignore expired instructions. Valid modes are Enable, Low, and Disable. Do not infer mode changes from general quality language. Persist activation and mode changes by default; preserve a valid stored mode on reinvocation without a new selection. Temporary/task-only/session-only mode requests and status queries do not write this file. Unqualified temporary requests are task-only. Task-only overrides expire after the task's final delivery; session-only overrides expire at session end. On expiry, discard the override and restore the valid stored mode or Low. Any later explicit mode instruction replaces the override. Never persist test authorization.

### Engineering modes

- Enable: Add proportionate handling for concrete, relevant failures and useful explanations. Do not design for hypothetical future requirements. Automatic validation remains preliminary only.
- Low: Default. Keep necessary checks and brief comments with real information. Do not proactively add extra fallback layers, generic frameworks, or future extension points. Automatic validation remains preliminary only.
- Disable: Add no optional defensive handling, explanatory comments, compatibility layers, or hardening. Implement the present requirements and their necessary parts. Preliminary validation still applies.

In every mode, retain explicit requirements, known current behavior, correctness, relevant platform/API contracts, and protections necessary at the current trust boundary or against directly exposed data loss. Speculative future failures are not necessary requirements. Mode changes do not authorize deleting existing protections, tests, comments, or quality gates.

Require a present requirement or concrete relevant failure before adding discretionary work. Even Enable does not authorize retry systems, logging infrastructure, configuration switches, compatibility matrices, unrelated refactors, or backend architecture changes just to make a local task robust.

### Comments

Do not add narration of obvious code, banners for every component or CSS section, repeated type information, or TODOs for hypothetical features. Keep required licenses, tool directives, required API documentation, and explanations of non-obvious constraints whose omission would invite an incorrect change. Disable excludes discretionary explanations, not these necessary comments. Do not perform a repository-wide comment-removal sweep.

### Validation and authorization

By default choose at most one relevant build, compile, type, or static check, up to three bounded smoke scenarios, and a brief review of changed code. These are ceilings, not mandatory checklists. Select representative rendering and the primary interaction for UI changes; do not enumerate every page, device, and browser. Do not add tests that merely mirror the implementation.

Inspect command definitions and lifecycle hooks. Judge actual coverage and effects, not command count: a command that runs a full suite, audit, or deployment is outside preliminary validation. Do not duplicate successful equivalent checks. Fix introduced defects locally and rerun the affected failed check; do not expand into a repository-wide audit. Report unrelated existing failures and continue unaffected authorized work. The allowance applies to the task/delivery as a whole, including all subagents.

Full functional testing, comprehensive regression, security audits, broad end-to-end testing, and stress testing require an explicit user request specifying the scope. Concrete requests to test named flows authorize only those flows. Authorization applies to this task and specified scope only; never store it as a default. Continue, finish it, check it, make it more robust, and switching to Enable do not grant broad testing permission. Disable does not stop preliminary checks. Preserve required quality gates and obey higher-priority instructions.

### Messages and delivery

Start every user-facing text message, including progress and final responses, with exactly one English line: Defensive Construction: followed by the effective mode, for example Defensive Construction: Low. Use the user's preferred language for the rest. Do not add routine state explanations or place the status banner in tool arguments, generated artifacts, source comments, repository files, or application UI. A required mode parameter is operational data, not a status banner.

Once at each delivery after implementation or modification, briefly name the checks actually run, their outcomes, and broader testing not run. Example: Validation: build and primary-flow smoke check passed; full functional and security testing not run. Accurately report failures, unrun checks, and environment blockers; do not claim full validation from a build. If broader testing was requested, report its actual scope and result. Do not repeat this statement in planning, progress, pure discussion, status queries, or mode switches.

### Persistence

Read the project-root Soul.md before writing. Update only this managed block, keep all content outside it unchanged, do not duplicate the block, and read back to confirm the selected mode and complete rules. Leave incomplete, reversed, or duplicate markers unchanged and report failed persistence. If the stored mode is invalid, use Low in-session and do not replace it without an explicit persistent selection. Temporary modes never overwrite the stored setting. If files are inaccessible or the root is unclear, apply the resolved mode in-session and report that it was not saved. Do not edit AGENTS.md or global configuration without the user's request. Soul.md requires an explicit instruction entry point for automatic cross-session loading.
<!-- defensive-construction:end -->
```
