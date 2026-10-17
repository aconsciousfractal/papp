# OPERA: corrected measurement and preserved history

Portable adaptation of the updated S2 note. Internal paths and edition
housekeeping are adapted; the scientific account is retained. This delivered
adaptation has not received a new human usability test.

**Question.** How does the corrected primary source change the conclusion
supported by OPERA's initial timing report?

**Current result.** [OPERA v4](https://arxiv.org/abs/1109.4897v4) reports
`delta_t = TOF_c - TOF_nu = 6.5 +/- 7.4 (stat.) +8.3/-8.0 (sys.) ns`:
positive means earlier arrival. Its `(v-c)/c = (2.7 +/- 3.1 (stat.)
+3.4/-3.3 (sys.)) x 10^-6` is compatible with zero. This distribution comparison
uses 15,223 selected 2009-2011 interactions; the CNGS beam's mean energy is
17 GeV. See section 8, printed pages 24-25 (physical PDF pages 27-28).

**What changed.** An improperly connected optical fibre added 73.2 ns delay,
underestimating flight time. An oscillator frequency excess of 0.124 ppm
overestimated event timestamps by up to 74 ns, acting oppositely and depending
on position within the acquisition cycle (section 6.1, printed pages 15-18).
The corrected analysis replaces the anomalous physical interpretation.

**Decisive limit.** Interpretation still depends on calibrated timing,
representative waveforms and distance estimates. Velocity conversion uses the
730.085 km effective baseline from the simulated mean decay point. Keep the
statistical and asymmetric systematic uncertainties separate. Compatibility
within these errors establishes neither exact equality nor a universal theorem
about neutrino velocities (sections 8 and 10).

**What survives.** S1 reported an unresolved anomaly under its original
conditions. That remains a superseded historical report, not current support
for faster-than-light neutrinos. [Historical adaptation](BEFORE.md) retains that account;
[SOURCES.json](SOURCES.json) identifies the exact original note consulted and
its subsequent checkpoint separately.

**Evidence.** OPERA Collaboration, *Measurement of the neutrino velocity with
the OPERA detector in the CNGS beam*, arXiv:1109.4897v4, 12 July 2012.
[Result: physical page 28](https://arxiv.org/pdf/1109.4897v4#page=28) is printed
page 25; [conclusion: physical page 33](https://arxiv.org/pdf/1109.4897v4#page=33)
is printed page 30. [Source identity](SOURCES.json) separately records
version, selectors and original byte identity; the PDF is not bundled.
No experimental replay or independent physical verification was performed.

**Checkpoint and next action.** This documentary comparison is complete:
the corrected account replaces the old physical interpretation, while the
historical result remains accessible with its warning. At the next source or
requirement change, inspect affected uses and reconcile them before relying on
this conclusion. The [maintenance guide](../../MAINTENANCE.md) describes that
manual step. This is a suggested future action, not a second completed test.

Responsible role: documentary evaluation maintainer.
