# Worked example contributed by Alexandre Couret, prepared with AI assistance and adapted for PAPP by Oleksiy Babanskyy.
# Attribution edition: PAPP/math-repair-example-0.1.0; see ../../../REUSE_NOTICE.md.
# Executable logic retained from the received LAB-03 source.
"""Exact finite-group calculations. Standard library only; no network or floats."""
from __future__ import annotations
from itertools import product, permutations
from math import gcd, prod, isqrt
from typing import Iterable, Sequence

Vector = tuple[int, ...]

class FiniteAbelianGroup:
    def __init__(self, moduli: Sequence[int]):
        if not moduli or any(type(n) is not int or n < 1 for n in moduli):
            raise ValueError('Positive integer cyclic factors required')
        self.moduli = tuple(moduli)
        self.elements = tuple(product(*(range(n) for n in moduli)))
        self.index = {e:i for i,e in enumerate(self.elements)}
        self.n = len(self.elements)
        self.zero = self.index[(0,)*len(moduli)]
        self.add_table = tuple(tuple(self.index[tuple((a+b)%n for a,b,n in zip(x,y,self.moduli))]
                                    for y in self.elements) for x in self.elements)
        self.neg = tuple(self.index[tuple((-a)%n for a,n in zip(x,self.moduli))] for x in self.elements)

    def multiply(self, k: int) -> tuple[int,...]:
        return tuple(self.index[tuple((k*a)%n for a,n in zip(x,self.moduli))] for x in self.elements)

    def validate(self, f: Sequence[int]) -> Vector:
        if len(f) != self.n or any(type(a) is not int or a < 0 for a in f):
            raise ValueError('Expected one nonnegative integer per labelled group element')
        return tuple(f)

    def convolve(self, f: Sequence[int], g: Sequence[int]) -> Vector:
        f,g = self.validate(f),self.validate(g)
        out=[0]*self.n
        for i,a in enumerate(f):
            if a:
                for j,b in enumerate(g):
                    if b: out[self.add_table[i][j]] += a*b
        return tuple(out)

    def power(self, f: Sequence[int], k:int) -> Vector:
        if type(k) is not int or k<1: raise ValueError('Positive convolution power required')
        f=self.validate(f); out=f
        for _ in range(k-1): out=self.convolve(out,f)
        return out

    def push(self, f: Sequence[int], p:int) -> Vector:
        """Push coefficients along g -> pg. This is NOT convolution."""
        f=self.validate(f); out=[0]*self.n
        for i,j in enumerate(self.multiply(p)): out[j]+=f[i]
        return tuple(out)

    def indicator(self, support: Iterable[int]) -> Vector:
        support=tuple(support)
        if len(set(support))!=len(support) or any(type(i) is not int or i<0 or i>=self.n for i in support):
            raise ValueError('Support must be a subset of valid labelled indices')
        return tuple(int(i in support) for i in range(self.n))

    def support(self, mask:int) -> tuple[int,...]:
        if type(mask) is not int or mask<0 or mask>=1<<self.n: raise ValueError('Bad mask')
        return tuple(i for i in range(self.n) if (mask>>i)&1)


def is_prime(p:int)->bool:
    return type(p) is int and p>=2 and all(p%d for d in range(2,isqrt(p)+1))

def square_direct(n:int, support:Iterable[int])->Vector:
    """Second implementation: ordered tuple enumeration in the cyclic group."""
    G=FiniteAbelianGroup((n,)); support=tuple(support); G.indicator(support)
    return tuple(sum((a+b)%n==x for a in support for b in support) for x in range(n))

def correlation(n:int, support:Iterable[int])->Vector:
    G=FiniteAbelianGroup((n,)); support=tuple(support); G.indicator(support)
    return tuple(sum((b-a)%n==x for a in support for b in support) for x in range(n))

def cyclic_orbit(n:int,support:Iterable[int],mode:str)->set[tuple[int,...]]:
    support=tuple(support)
    FiniteAbelianGroup((n,)).indicator(support)
    if mode=='translation': units=(1,)
    elif mode=='dihedral': units=(1,-1)
    elif mode=='affine': units=tuple(u for u in range(n) if gcd(u,n)==1)
    else: raise ValueError('Unknown equivalence mode')
    return {tuple(sorted((u*x+t)%n for x in support)) for u in units for t in range(n)}

def decode_digit_power(G:FiniteAbelianGroup, observed:Sequence[int], p:int,
                       allowed:Iterable[int], exponent:int=1)->dict:
    """Decode digits 0..p-1 from power p**exponent; then check FULL integer data.

    Raises for unsupported noninjective domain. Does not conclude failure of
    other recovery methods. A mismatch rejects the input as realizable under
    this precise model, not as a physical measurement.
    """
    if not is_prime(p) or type(exponent) is not int or exponent<1:
        raise ValueError('Prime p and positive exponent required')
    obs=G.validate(observed); D=tuple(allowed); G.indicator(D)
    k=p**exponent; mul=G.multiply(k)
    if len({mul[i] for i in D})!=len(D):
        raise ValueError('Declared allowed domain is not injective under multiplication by p**exponent')
    f=[0]*G.n
    for i in D: f[i]=obs[mul[i]]%p
    matches=G.power(f,k)==obs
    return {'status':'unique_match' if matches else 'inconsistent_data',
            'candidate':f, 'matches_full_integer_data':matches, 'p':p, 'power':k}

def verify_collision(n:int,a:Sequence[int],b:Sequence[int])->dict:
    G=FiniteAbelianGroup((n,)); va=G.indicator(a); vb=G.indicator(b)
    same=G.power(va,2)==G.power(vb,2)
    eq={m:tuple(sorted(b)) in cyclic_orbit(n,a,m) for m in ('translation','dihedral','affine')}
    return {'n':n,'A':list(a),'B':list(b),'same_integer_square':same,
            'distinct':va!=vb, 'square_A':list(G.power(va,2)),
            'square_B':list(G.power(vb,2)), 'equivalences':eq,
            'refutes_exact':same and va!=vb,
            'refutes_up_to_translation':same and not eq['translation'],
            'refutes_up_to_dihedral':same and not eq['dihedral'],
            'refutes_up_to_affine':same and not eq['affine']}

def s3_control()->dict:
    elems=tuple(permutations(range(3))); idx={p:i for i,p in enumerate(elems)}
    def comp(a,b): return tuple(a[b[i]] for i in range(3))
    a,b=(1,0,2),(0,2,1); counts=[0]*6; diagonal=[0]*6
    for x in (a,b):
        diagonal[idx[comp(x,x)]]+=1
        for y in (a,b): counts[idx[comp(x,y)]]+=1
    return {'elements':[list(x) for x in elems], 'A':[list(a),list(b)],
            'square':counts, 'diagonal':diagonal,
            'frobenius_mod2_fails': [v%2 for v in counts]!=[v%2 for v in diagonal]}
