# Repairing a claim without losing valid results

**Worked example contributed by Alexandre Couret, prepared with AI assistance and adapted for PAPP by Oleksiy Babanskyy.**

*Example package 0.1.0 · optional mathematical companion to PAPP 1.0.3.*

## Count pairs on a clock

Place labels 0,...,n-1 around a clock, adding modulo n: on a six-position
clock, 4+3 lands at 1. An unknown subset S marks some positions. For each
label x, observe the exact integer count

\[
R_S(x)=\#\{(a,b)\in S\times S:a+b\equiv x\pmod n\}.
\]

Pairs are ordered, and self-pairs count: (a,b) and (b,a) are separate when
a differs from b. Every count retains its label. Can these labelled counts
identify S exactly? This pair-count vector is called its convolution square.
We are recovering a binary subset, without identifying translated copies.

## The valid theorem

**If n is odd, R_S uniquely determines every subset S of C_n.** Here C_n
means the labels with addition modulo n. Pair each off-diagonal (a,b) with
(b,a). Their combined contribution is even. Thus, for every n,

\[
R_S(x)\equiv\sum_{2a=x}\mathbf{1}_S(a)\pmod 2,
\]

where the indicator is 1 at marked positions and 0 elsewhere. For odd n,
doubling permutes the labels because 2 is invertible modulo n: each equation
2a=x has exactly one solution.
Consequently, the parity of R_S(2y) recovers the membership bit at y. This
argument proves the theorem for all odd orders; enumerating small clocks
would establish only those finite checks.

## The extension that fails

Now remove "odd" and claim the same exact recovery for every n. On C6,

\[
S=\{0,1,2\},\qquad T=\{3,4,5\},\qquad
R_S=R_T=(1,2,3,2,1,0).
\]

The displayed vector lists coefficients at labels 0 through 5. Distinct
subsets give identical observations, so the unrestricted claim is false.
This does not invalidate the odd-order proof or assert that every even-order
subset is ambiguous. Also T=S+3: this particular pair does **not** refute
recovery up to translation. An objection needs the same precision as a proof.

## Keep the identity; recover a restricted result

For an even clock n=2m, opposite (antipodal) positions are y and y+m.
The parity identity still holds and reads

\[
R_S(2y)\equiv\mathbf{1}_S(y)+\mathbf{1}_S(y+m)\pmod 2.
\]

It preserves parity of occupancy of antipodal pairs, rather than individual
membership in general. Suppose a fixed allowed domain D is **known**, S is
contained in D, and D contains at most one position from each antipodal pair.
For y in D, the other position is forbidden. The formula therefore recovers
every permitted membership bit; outside D the indicator is zero. Exact
recovery is restored on this declared class.

The word "known" matters. Merely assuming that S contains at most one
position from each pair is insufficient: {0} and {3} in C6 both satisfy that
restriction and both give (1,0,0,0,0,0). Their allowed representatives cannot
be inferred from that observation. A known domain such as D={0,1,2} excludes
this ambiguity.

## A sufficient handoff

**Before:** "Exact recovery for odd cyclic orders is proved by parity. The
proposed extension to all orders remains to be checked."

**After:** "Retain the odd-order theorem and the all-order parity identity.
Withdraw the unrestricted extension by the C6 collision. Retain recovery on
a known domain with injective doubling. The proof is above; run
`python check_examples.py` for the selected finite examples. This closes the
extension check. Resume from these qualified statements if a new question
requires further work."

This illustrates existing PAPP guidance: reconcile the affected conclusion
and its dependent summaries while preserving supported results. The
[small checker](check_examples.py) verifies examples; it is neither the general
proof nor a measurement of PAPP's effectiveness. Optional C8/Frobenius
extensions are in the [accompanying note](supplementary/NOTE_FOR_OLEKSIY_EN.pdf).
See [attribution and references](ATTRIBUTION.md) and the [reuse notice](REUSE_NOTICE.md).
