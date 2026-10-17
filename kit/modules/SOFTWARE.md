# Software work

Use this module when the task changes software behavior or depends on a
software result. Start by identifying the behavior the user needs, the relevant
inputs and outputs, and the completion condition. Find the existing issue,
requirements, code and adequate checks before creating anything. Keep the
account in the issue, note or other native checkpoint already used by the
project; this module does not require another file or evidence form.

For a reported failure, distinguish the expected behavior from the actual
error. Preserve the smallest useful reproduction, observed message or output,
and relevant environment details. State when the failure has not been
reproduced. A plausible explanation is a hypothesis until inspection or a
check supports it.

Choose the smallest adequate set of cases for the change and its consequences.
Include the failing case and relevant boundaries or regressions where they
could reveal a meaningful defect. Record the commands actually run, inputs or
fixtures needed to repeat them, and observed outcomes. Explain what those
checks cover and what remains unchecked. Passing selected cases supports
those cases; it does not establish all-input correctness, security or general
compatibility. If a required environment is unavailable, retain that limit.

For an execution claim, identify the tested code revision or snapshot and the
relevant runtime and inputs in the existing account; an earlier run does not
itself establish that changed code was tested.

When code, an upstream API or a requirement changes, revisit the conclusions
that depend on it. Identify which checked behaviors still apply, which need
new evidence, and which remain unresolved. Update the checkpoint for that
scope without rewriting the old observation as if it tested the new version.
An existing test suite may be sufficient; do not add tests that only repeat
implementation details or repeatedly broaden testing after adequate checks
have passed.

**Example.** A parser drops a final row when the input has no trailing newline.
Keep that input in the issue, compare expected and observed rows, fix the
parser, and check the failing input plus the equivalent newline-terminated
case. Report those outcomes and any relevant input formats left unchecked.

**When this is unnecessary.** Correcting a comment or adjusting cosmetic
spacing without changing behavior usually needs a direct inspection, not a
new test campaign or software record.

**Dependent-use limit.** If deployment requires a supported platform that was
not checked, defer the deployment conclusion for that platform. Continue
authorized work that does not rely on it, and identify the missing check.
