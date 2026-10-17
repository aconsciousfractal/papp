# Empirical research

Use this module when a conclusion depends on observations, measurements or
data analysis. State the question, intended scope and kind of inference before
selecting an analysis. Reuse a sufficient notebook, data description or study
note; preserve the necessary meanings there instead of creating an empty
ledger or universal evidence form.

Identify the observations actually used, their origin and relevant version,
the measured quantities and units, and the observation or sampling period.
Describe transformations, filters, exclusions and missingness that affect the
result. Distinguish a missing value from zero and explain any imputation.
Keep raw observations or an accessible source separate from derived values
where needed to inspect the calculation. State access limitations rather than
implying that another person can reproduce unavailable data.

Connect inference to the study design. Identify the population or system
sampled, selection process, comparison conditions and relevant uncertainty.
Separate a descriptive result for the observed sample from an estimate or
generalization beyond it. Explain assumptions that affect interpretation,
including dependence among observations or possible confounding. A correlation
does not by itself establish causation. A negative result may reflect limited
power, measurement sensitivity or scope; it is not automatically a refutation
of every version of a hypothesis. State which prediction was tested and under
what conditions.

Distinguish exploratory findings from confirmatory claims. Record consequential
analysis choices, including metrics, subgroups, models, stopping rules and the
family of comparisons, and identify choices made or changed after inspecting
results. Before presenting a selected finding as confirmed, use an inferential
treatment appropriate to that selection or a separate confirmatory check whose
design addresses it. Preserve exploratory findings with their qualifications;
preregistration or one particular correction is not required for every task.

Keep calculations auditable at the level needed for the conclusion. Provide
the formula, notebook cells, script or calculation steps and the inputs they
use. Select adequate checks for meaningful errors: units, denominators,
transformations, representative hand calculations, or sensitivity to a
consequential choice. Record checks actually performed and their outcomes.
Do not report an intended check as observed evidence. Further checks are
needed when uncertainty or consequence warrants them, not merely to fill a
template. If data or assumptions change, reconcile affected results and
preserve the earlier result under its original scope.

For simulation claims, distinguish model assumptions, checks of the numerical
implementation, calibration data and evidence for predictive performance.
Agreement with calibration data alone does not establish predictive validity
beyond those data.

**Example.** Compare temperature readings from two periods after converting
both to the same unit. Identify the sensors and periods, report missing
readings and the actual aggregation, and check one conversion and denominator.
A difference in these observations alone does not establish its cause.

**When this is unnecessary.** Relaying an already documented measurement with
its unit and qualification need not create a fresh analysis notebook.

**Dependent-use limit.** If a causal conclusion requires a design or control
that is absent, refuse that inference. Keep the supported descriptive result
and continue authorized analysis that does not depend on the causal claim.
