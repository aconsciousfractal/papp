# Correcting a claim without losing its valid mathematics

**Worked example contributed by Alexandre Couret, prepared with AI assistance and adapted for PAPP by Oleksiy Babanskyy.**

*Attributed source exposition for PAPP/math-repair-example-0.1.0. The following is the received
LAB-03 mathematical note. References to included files and historical checks
refer to that original kit; see [this package's supplementary scope](README.md)
and [permission notice](../REUSE_NOTICE.md).*

Prepared for Alexandre Couret with AI assistance, 24 October 2026. Candidate contribution to Oleksiy Babanskyy's PAPP; no external submission. The synthetic false statements below are NOT errors found in Oleksiy's work. No novelty or independent-review claim is made.

## 1. Observable, object class and equivalence

Let G be a finite abelian group, written additively. For nonnegative integer functions f,g on G define

    (f*g)(x) = sum_{a+b=x} f(a)g(b).

The data are exact integers labelled by x. Unless explicitly weakened, recovery means equality of functions, not translation, reflection, affine equivalence, spectra or graph isomorphism. For a support S we use its indicator 1_S, and R_S=1_S*1_S. The count is ordered, and includes diagonal pairs. Those are substantive hypotheses, not notation.

## 2. Binary square: the exact surviving statement

Pair (a,b) with (b,a). For a!=b these contribute an even number to the same coefficient, because G is abelian. Hence

    R_S(x) mod 2 = sum_{2a=x} 1_S(a) mod 2.                 (1)

On an odd-order cyclic group, multiplication by 2 is bijective, so 1_S(y)=R_S(2y) mod 2. More generally the same proof works on every finite abelian group with trivial two-torsion.

On C_(2m), (1) reads

    R_S(2y) mod 2 = 1_S(y)+1_S(y+m) mod 2.

This retains the parity of occupancy of each antipodal pair, not necessarily its occupancy count. If S is restricted to a KNOWN set D containing at most one representative of each pair, the individual indicator bits are recovered. Merely knowing "at most one of each pair occurs" without knowing the allowed representatives is insufficient: {0} and {m} still collide.

## 3. A necessary-and-sufficient domain criterion

**Proposition (binary).** For a fixed known D subset G, the map S -> R_S is injective on the entire class of subsets S subset D if and only if a -> 2a is injective on D.

Proof. If doubling is injective on D, (1) at x=2a has at most one possible contributing point in D, so it recovers 1_S(a). Conversely, if a!=b in D and 2a=2b, the singleton supports {a} and {b} have identical integer squares. QED.

This is a complete criterion for that object class. The necessity argument uses singletons. It must NOT be exported unchanged to a class of supports of fixed size three, or to the boundary theorem discussed in earlier correspondence. No such theorem is audited here.

The largest possible admissible D contains one representative from each fibre of doubling. Its size is |2G|=|G|/|G[2]|. This concerns this particular recovery-by-domain mechanism; it does not classify all recoverable individual supports outside such a domain.

## 4. Prime and prime-power extension

Let p be prime, r>=1 and q=p^r. For any integer f, in the commutative group algebra F_p[G], the Frobenius endomorphism and its iterates give

    f^{*q}(x) mod p = sum_{qa=x} f(a) mod p.                (2)

Indeed, if F=sum_a (f(a) mod p) e_a, then e_a e_b=e_(a+b), and
F^(p^r)=sum_a (f(a) mod p)^(p^r) e_(p^r a)=sum_a (f(a) mod p)e_(q a).
The algebra is commutative because G is abelian; coefficients in F_p are fixed by Frobenius.

**Proposition (digits).** On the class of all functions supported in a fixed known D with values in {0,...,p-1}, the map f -> f^{*q} is injective if and only if a -> qa is injective on D. The same iff holds for indicators on that D.

Proof. Sufficiency follows from (2): the coefficient at qa recovers the unique digit f(a). Necessity is again witnessed by two colliding singleton delta functions. This includes the empty domain. If p is coprime to |G|, the map is bijective on G, so D=G is allowed. QED.

A nonnegative vector submitted as observed data may be inconsistent with this model. Decode its residues, then recompute the FULL integer convolution power before accepting a match. Matching residues alone is not an exact data certificate.

**Information explicitly lost.** For the REDUCED observation (2), viewed on all F_p-valued functions, the map is linear with one independent row for every nonempty fibre of a -> qa. Its rank is |qG|; its kernel has dimension |G|-|qG|. Every attainable reduced vector has p^(|G|-|qG|) preimages. This is NOT the fibre size of the full integer convolution observation: reducing modulo p discards information.

These are elementary uses of a classical Frobenius identity, not a claim of new mathematics. Primary references for that identity: The Stacks Project, Section 33.36, and Mathlib.Algebra.CharP.Frobenius. Reading mathlib documentation is not compiling this proof in Lean.

## 5. A ladder of witnesses, each with a limited scope

**Exact recovery only.** In C6, {0,1,2} and {3,4,5} both have square (1,2,3,2,1,0). They differ by translation by 3. This pair does not refute recovery up to translation.

**Not translation, but reflection.** In C6, {0,1,4} and {0,2,5} both have square (1,2,2,0,2,2). They are not translates, but the second is the negative of the first. This pair does not refute dihedral recovery.

**Not even affine.** In C8, A={0,1,3,4} and B={1,2,3,6} have square

    (2,2,1,2,4,2,1,2).

They are not related by x -> ux+t for any unit u mod 8 and any t. Human check: A has exactly one antipodal pair {0,4}; B has exactly one, {2,6}. An affine map would send the former to the latter, forcing t=2 or 6. But sum A=0 mod 8, whereas sum B=4 mod 8. An affine image would have sum u*0+4t=0 mod 8 for either forced t, a contradiction. The checker also enumerates all 32 affine maps. No claim about arbitrary Cayley graph isomorphism is made.

**Binary coefficients matter even at odd order.** In C3, the different nonnegative weight vectors (0,1,2) and (2,1,0) both square to (4,4,1). Thus the odd-order indicator result cannot simply be promoted to arbitrary nonnegative weights.

**Commutativity matters to the identity.** In S3, let a=(12), b=(23). For f=delta_a+delta_b, f*f=2 delta_e+delta_ab+delta_ba. The two cross terms occupy distinct group elements and remain modulo 2. The diagonal pushforward alone is zero modulo 2. This refutes the naive noncommutative Frobenius identity, not every conceivable recovery theorem on S3.

**Prime versus composite modulus.** In C3, f=(1,1,0) has fourth convolution power (5,5,6). Modulo 4 this is not the pushforward along a -> 4a, which is (1,1,0). The correct iterated Frobenius statement uses exponent 4 and modulus 2, not modulus 4.

## 6. What was executed

All arithmetic uses Python integers and the standard library. The main run checks all 32,764 binary cyclic supports for 2<=n<=14. It separately checks 2,044 allowed domains for 2<=n<=10, representing 88,569 pairs (D,S) with S subset D, against the binary iff criterion. Digit tests cover 7,184 vectors: p=3 for 1<=n<=7 and p=5 for 1<=n<=5. Product-group tests cover 1,696 binary vectors in C2xC2, C2xC3, C2xC4 and C3xC3 at p=2 and p=3, plus their fixed-transversal checks. Iterated-prime-power tests cover 572 binary cases.

These counts overlap in object families and must not be added into a count of independent experiments. None is a trial of an assistant. The general propositions are justified by the written arguments, not by these counts.

An exploratory bounded collision search found the C8 witness above. The search does not establish global minimality or originality. The scripts, selected results and exact checked ranges are included. All code and two implementations were produced in the same assisted session, so their agreement is not independent review.

## 7. What remains unestablished

No comparative assistant experiment; no new-context human/agent handoff trial; no Lean compilation; no audit of Oleksiy's private agent or FCIG; no proof of novelty; no endorsement of the earlier private theorem package. The bounded tests support their finite conclusions. They do not repair these missing forms of evidence.

## References and source attribution

PAPP core, MATHEMATICS, CONTRACT, COMPATIBILITY and EDITION, by Oleksiy Babanskyy, pinned at ed4a392af8f09ec8fc7b5b3bdd2452bbd246722b. Main was checked to point to that commit during preparation. Exact selected blobs are included under the upstream MIT license; the guide is not modified. See upstream/SOURCE_SNAPSHOT.json.

Frobenius background:
- https://stacks.math.columbia.edu/tag/0CC6
- https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Frobenius.html
