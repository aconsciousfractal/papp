# Attribution and mathematical references

**Worked example contributed by Alexandre Couret, prepared with AI assistance and adapted for PAPP by Oleksiy Babanskyy.**

This credit applies to the mathematical worked example and its accompanying
note and reproducible code. It does not assign Alexandre coauthorship of the
whole PAPP protocol, ownership of classical mathematical facts, independent
review credit, or endorsement of another research programme.

The contributor approved this exact credit line in a follow-up relayed by
Oleksiy. It is visible near the beginning of the example page, on the first
page of the attributed PDF, in the mathematical note and source headers,
and in the supplementary README. Oleksiy will retain this attribution and
the relevant mathematical references in release copies and adaptations he
prepares under that permission. See [the reuse notice](REUSE_NOTICE.md).

## Sources and adaptations

Source contribution: *PAPP-MATH-REPAIR-LAB-03*, dated 24 October 2026.
The original archive and six-page PDF remain preserved unchanged in the
internal project. This companion identifies attributed adaptations separately.

- `README.md`: short adaptation of the worked argument and handoff; its
  mathematical body comes from the previously checked internal candidate.
- `check_examples.py`: simplified ordered-pair checker; this revision changes
  its credit header only, preserving the tested executable logic.
- `supplementary/NOTE_FOR_OLEKSIY_EN.pdf`: six-page adapted note. Page 1 carries
  visible credit; page 5 supersedes the historical attribution-waiver wording;
  page 6 gives the companion's available commands and labels the historical
  LAB-03 source record. Mathematical arguments and references are retained.
- `supplementary/MATHEMATICS_EN.md`: the received mathematical exposition
  with an attribution/context preamble; original arguments and references retained.
- `supplementary/code/`: received mathematical replay and arithmetic module,
  with credit comments added; executable syntax is unchanged.
- `supplementary/exact_results.json`: the original finite result, reproduced
  byte for byte as historical evidence; no new model study is claimed.

## Mathematical provenance

The main page gives its elementary ordered-pair parity proof. The optional
prime-power extension uses the classical Frobenius identity in a commutative
group algebra in characteristic p. Retain the contribution's references:

- [The Stacks Project, Section 33.36, Frobenii, tag 0CC6](https://stacks.math.columbia.edu/tag/0CC6).
- [Mathlib.Algebra.CharP.Frobenius](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Frobenius.html).

PAPP's original guidance by Oleksiy Babanskyy is identified separately as
PAPP/documentary-1.0.3. This example illustrates its existing guidance; it
does not establish novelty, formal Lean verification, independent mathematical
review, or a measured improvement in PAPP effectiveness.

Package identity: **PAPP/math-repair-example-0.1.0**. [Edition and file inventory](EDITION.md).
