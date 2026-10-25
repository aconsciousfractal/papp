# Accompanying mathematical material

**Worked example contributed by Alexandre Couret, prepared with AI assistance and adapted for PAPP by Oleksiy Babanskyy.**

Package: **PAPP/math-repair-example-0.1.0**. See [permission](../REUSE_NOTICE.md)
and [attribution and references](../ATTRIBUTION.md).

- [Adapted six-page note](NOTE_FOR_OLEKSIY_EN.pdf): visible credit on page 1;
  the superseded attribution-waiver wording corrected on page 5; companion
  commands and the historical LAB-03 record clearly separated on page 6.
  Existing page numbers, mathematical arguments and references are retained.
- [Mathematical exposition](MATHEMATICS_EN.md): source exposition with an
  attribution/context preamble. Wider C8 and Frobenius material is optional.
- [Historical exact result](exact_results.json): original replay output,
  unchanged bytes; this is finite arithmetic evidence, not an AI evaluation.
- `code/replay.py` and `code/src/exact_math.py`: mathematical replay sources
  with credit comments added, preserving executable syntax.

For an optional fresh arithmetic run, from `supplementary/code/` use:

```text
python replay.py --output my-run.json
```

Python 3.10+ standard library is sufficient. Choose your own output path;
this does not rerun a model or a formal proof kernel.

The original note describes the larger LAB-03 kit, including its development
cases, unit tests and evaluation proposal. Its relative paths and historical
run counts refer to that received kit. This smaller companion does not bundle
that evaluation infrastructure or its answer key. Use this file and the package
manifest for the actual companion contents; use the short example for its
self-contained proof. The original packet is preserved in the internal project.
