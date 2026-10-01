---
name: lean-build
description: Control optional defensive engineering and test scope when the user asks for lean implementation, less overengineering, or a Defensive Construction mode.
---

# lean-build

Complete the requested work with the least engineering needed for its actual requirements. Control discretionary defensive construction; do not reduce feature completeness or necessary correctness.

## 1. Activate and resolve state

Identify the current project root from the user's project context or repository root; do not assume the skill installation directory is the target project. Read its `Soul.md` if present.

Use the latest explicit user mode instruction still applicable to this project and scope first, then an active temporary override, then the valid stored mode, then `Low`. Ignore expired instructions. Accept only `Enable`, `Low`, and `Disable`; do not infer a mode from words such as "robust" or "simple."

Persist activation and explicit mode changes by default. Preserve an existing valid mode on reinvocation without a new selection. Read [persistence.md](references/persistence.md) before writing. A temporary/task-only/session-only request changes session state without writing `Soul.md`; a status query is also read-only. An unqualified temporary request is task-only. Task-only overrides expire after the task's final delivery; session-only overrides expire at session end. On expiry, discard the override and restore the valid stored mode or `Low`. Any later explicit mode instruction replaces the override. Test authorization is separate session state and is never persisted.

If the project root is unclear or files are inaccessible, apply the resolved mode in this session and briefly report that persistence was not completed. Do not claim a saved policy or change another project's files.

## 2. Choose the engineering level

| Mode | Discretionary engineering | Automatic validation |
| --- | --- | --- |
| `Enable` | Add proportionate handling for concrete, relevant failure cases; retain useful explanations. Avoid speculative future requirements. | Preliminary only |
| `Low` | Default. Keep necessary checks and brief comments that carry real information. Avoid extra fallback layers, generic frameworks, and future extension points. | Preliminary only |
| `Disable` | Add no optional defensive handling, explanatory comments, compatibility layers, or hardening. Implement the current requirements and their necessary parts. | Preliminary only |

Every mode must satisfy explicit requirements, known current behavior, correctness, relevant platform/API contracts, and protections necessary at the current trust boundary or against directly exposed data loss. A speculative future failure does not make an addition necessary. Fix defects introduced by your changes.

Before adding discretionary work, identify the present requirement or concrete relevant failure it serves. If neither exists, omit it. Even `Enable` does not authorize retry systems, logging infrastructure, configuration switches, compatibility matrices, unrelated refactors, or backend architecture changes merely to make a local change "robust."

Mode changes never authorize removing existing protections, tests, comments, or quality gates. Preserve required gates and follow higher-priority instructions. If they require broader validation, state the concrete requirement and its source; do not silently waive it or treat optional practices as required gates.

## 3. Keep comments purposeful

Do not add line-by-line narration of obvious code, banners for every component/CSS section, repeated type information, or TODOs for hypothetical features. Do not sweep the repository to remove existing comments.

Keep required license notices, tool directives, required API documentation, and explanations of non-obvious constraints whose omission would invite an incorrect change. In `Disable`, omit discretionary explanations; these necessary comments remain allowed.

## 4. Validate within the authorized scope

By default, choose at most one relevant build, compile, type, or static check, plus up to three bounded smoke scenarios and a brief review of the changed code. These are ceilings, not a checklist. For UI work, select representative rendering and the primary interaction; do not enumerate every page, device, and browser.

Read [validation.md](references/validation.md) when selecting commands, handling failures, or interpreting test requests. Inspect what a script actually executes, including lifecycle hooks. Count coverage and effects, not command count. A command that runs a full suite, audit, or deployment is outside preliminary validation. Do not invent a check when none is relevant.

Full functional testing, comprehensive regression, security audits, broad end-to-end testing, and stress testing require an explicit user request specifying that scope. A concrete request to test particular flows authorizes those flows without requiring a magic phrase. Authorization lasts for this task and specified scope only.

"Continue," "finish it," "check it," "make it more robust," and switching to `Enable` do not expand test authorization. `Disable` still permits preliminary checks. After a local fix, rerun the affected failed check; do not repeat successful equivalent checks or expand into a repository-wide audit.

## 5. Show state and report evidence

While active, start every user-facing text message, including progress and final responses, with exactly one line using the effective mode:

```text
Defensive Construction: Low
```

Replace `Low` with the actual mode. Keep the rest of the message in the user's preferred language. Do not add a status explanation unless needed. Do not prepend this line to tool arguments, source comments, generated artifacts, repository files, or application UI. A tool's required mode parameter is operational data, not a status banner.

At each delivery after implementation or modification, give one short validation statement naming checks actually run and their outcomes, and the broader testing not run. For example:

```text
Validation: build and primary-flow smoke check passed; full functional and security testing not run.
```

Report failures, unrun checks, and environment blockers accurately. Do not claim full validation from a build. Do not repeat the statement during planning, progress updates, pure discussion, status queries, or mode switches. If broader testing was explicitly requested, report its actual scope and result instead of using the default example.

## Conditional resources

- [Validation scope and examples](references/validation.md): read when choosing or expanding verification.
- [Persistence protocol and complete Soul.md block](references/persistence.md): read before saving project policy or discussing cross-session loading.
- [Soul.md update helper](scripts/update_soul.py): optional Python 3 standard-library helper; updates only the managed block and verifies the saved bytes. No helper is needed for temporary modes or status queries.
