# Validation scope

## Select preliminary checks

Use only checks that can provide useful evidence about the current change:

1. Inspect the relevant project command definitions and hooks before execution. Prefer one existing applicable build, compile, type, or static check. If a build already type-checks, do not run an equivalent type check too.
2. Choose zero to three small smoke scenarios directly affected by the change. One scenario is a bounded path with a concrete expected outcome, not a loop over the entire product. For UI work, representative rendering and the primary interaction are usually sufficient.
3. Briefly inspect the diff for scope drift and defects you introduced. Repair those locally.

For an instruction-only or documentation change, a relevant format/link check or scoped read-through may be sufficient. For a changed helper, exercise its important observable behavior. Do not add tests that merely mirror wording or implementation. Do not install a new testing stack for a small reversible change unless the task actually needs it.

Do not bypass protected environments, trigger deployment, or weaken a quality gate to make a preliminary command fit. When an existing command mixes a useful check with broader optional work, use a supported narrower command. If none exists, report the unavailable check accurately; do not run the broader command under the label "smoke test."

## Judge actual scope

| Situation | Decision |
| --- | --- |
| `build` invokes compilation and the same type checker | Run once; no duplicate type check. |
| `build` invokes all tests, an audit, or deployment hooks | Outside the default allowance; choose a bounded alternative. |
| One browser script loops over all routes, browsers, and devices | Broad testing despite being one command. |
| A bounded check fails because of the current patch | Fix the introduced defect, rerun that check. |
| A check exposes an unrelated pre-existing failure | Report it; continue authorized work that is unaffected. Do not start an unsolicited repair campaign. |
| A required instruction or gate specifies a broader suite | Preserve it and identify the concrete source; this skill cannot waive it. |

The ceiling is per implementation task/delivery, not per file, agent, retry, or message. Subagents share the same validation allowance; delegation does not multiply it. A necessary rerun after a fix verifies the same coverage rather than granting new coverage.

## Interpret user authorization

Explicit scope can be expressed naturally:

- "Run the entire regression suite" authorizes that suite for this task.
- "Test login, password reset, and session expiry on Chrome and Safari" authorizes those named flows and browsers.
- "Audit this new authentication endpoint for security" authorizes that endpoint audit, not an organization-wide scan.

General continuation and quality language does not authorize broad testing: "continue," "finish," "check it," "make it robust," and "Enable" keep the preliminary allowance. When scope is genuinely ambiguous and needed for the requested outcome, ask one focused question while completing independent work. Do not interrupt routine implementation simply to ask whether optional full testing should be run.

Authorization applies to the present task and named scope. Do not store it in `Soul.md`, convert it into a project default, or carry it into a later task. An authorized audit or test request still does not authorize unrelated implementation, deletion, deployment, or other external side effects.

## Report once at delivery

Describe actual evidence concisely. The validation sentence may use the user's language; the status line must remain English.

- Passed: `Validation: type check and save-flow smoke check passed; full functional and security testing not run.`
- Failed: `Validation: compilation failed at the changed import; smoke checks not run; full functional and security testing not run.`
- Blocked: `Validation: build unavailable because the required SDK is missing; diff review completed; full functional and security testing not run.`
- Documentation only: `Validation: skill format and reference links checked; runtime behavior not exercised; full functional and security testing not run.`

A scenario review shows how an agent interpreted the instructions in that evaluation; it does not establish reliable behavior across GPT models, projects, or future sessions.
