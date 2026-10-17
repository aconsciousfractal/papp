# OPERA: original report, historical snapshot

Portable adaptation of the original S1 note. The source was already superseded
when this historical account was written; it is not current evidence for
faster-than-light neutrinos. [AFTER](AFTER.md) is the reconciled successor.
Human findability feedback concerned the original bytes, not this adaptation.

**Question.** What did the initial measurement support, under which conditions?

**Result.** OPERA reported `delta_t = TOF_c - TOF_nu = 60.7 +/- 6.9 (stat.)
+/- 7.4 (sys.) ns`: positive means earlier arrival. This was a maximum-likelihood
shift between time distributions, using 16,111 events from 2009-2011, rather
than an individual neutrino's directly timed journey. The beam's mean energy
was 17 GeV. See S1, section 3, printed pages 7-8, and section 7, page 19.

The reported conversion `(v-c)/c = delta_t/(TOF'_c - delta_t)` yielded
`(2.48 +/- 0.28 (stat.) +/- 0.30 (sys.)) x 10^-5`, with claimed 6.0-sigma
significance. `TOF'_c` uses a 730.085 km effective neutrino baseline from the simulated
mean decay point; it is
distinct from the BCT-to-detector timing baseline (section 7, page 19).

**Decisive limit.** That physical interpretation depends on representative
proton waveforms, calibrated timing/synchronisation and distance estimates
(sections 3-7). The stated significance incorporates the quoted uncertainties;
it cannot exclude an unrecognised calibration error. The authors kept unknown
systematic effects open and supplied no theoretical interpretation
(Conclusions, page 22). Our supported conclusion is a historical report of an
unresolved timing anomaly under those conditions.

**Evidence.** OPERA Collaboration, *Measurement of the neutrino velocity with
the OPERA detector in the CNGS beam*, v1, 22 September 2011. Open the
[exact primary PDF](https://arxiv.org/pdf/1109.4897v1#page=19) at printed page 19;
page 22 carries the decisive qualification. Physical PDF page numbers match
these printed pages. [Source identity](SOURCES.json) records the exact version
and separate selectors. The PDF is linked, not bundled; byte identity does not
verify the experiment.

**Checkpoint at that stage.** The historical result and its limits were
recorded. The next action was reader consultation, followed by inspection of
the exact v4 paper to reconcile changed timing evidence. Those steps were
later completed as described in [the example account](README.md).

Responsible role: documentary evaluation maintainer. [Working guidance](../../kit/PAPP.md).
