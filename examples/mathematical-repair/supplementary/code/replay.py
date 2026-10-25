#!/usr/bin/env python3
# Worked example contributed by Alexandre Couret, prepared with AI assistance and adapted for PAPP by Oleksiy Babanskyy.
# Attribution edition: PAPP/math-repair-example-0.1.0; see ../../REUSE_NOTICE.md.
# Executable logic retained from the received LAB-03 source.
"""Run finite exact checks. No AI models, no formal kernel and no network."""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path
from itertools import product
from math import gcd
from src.exact_math import *
ROOT=Path(__file__).resolve().parent

def require(ok:bool, name:str)->None:
    if not ok: raise AssertionError(name)

def run()->dict:
    rows=[]; total=odd=even=0; atlas={}; ranges=[]
    for n in range(2,15):
        G=FiniteAbelianGroup((n,)); buckets={}; collisions=0
        for mask in range(1<<n):
            S=G.support(mask); f=G.indicator(S); R=G.power(f,2)
            require(R==square_direct(n,S),'ordered-pair implementation disagreement')
            require(tuple(v%2 for v in R)==tuple(v%2 for v in G.push(f,2)),'parity pushforward')
            if n%2:
                require(decode_digit_power(G,R,2,range(n))['candidate']==list(f),'odd recovery')
                odd+=1
            else: even+=1
            total+=1
            if R in buckets:
                collisions+=1
                for T in buckets[R]:
                    for mode in ('translation','dihedral','affine'):
                        if mode not in atlas and S not in cyclic_orbit(n,T,mode):
                            atlas[mode]=verify_collision(n,T,S)
                buckets[R].append(S)
            else: buckets[R]=[S]
        rows.append({'n':n,'supports':1<<n,'distinct_square_vectors':len(buckets),
                     'nonfirst_members_of_collision_fibres':collisions})
        print(f'cyclic n={n}: {1<<n} supports',file=sys.stderr)
    # ALL allowed domains, binary square: 3^n support/domain inclusions.
    domains=domain_functions=injective_domains=0
    for n in range(2,11):
        G=FiniteAbelianGroup((n,)); mult=G.multiply(2)
        for dmask in range(1<<n):
            D=G.support(dmask); expected=len({mult[i] for i in D})==len(D)
            seen=set(); injective=True
            for sub in range(1<<len(D)):
                S=tuple(D[i] for i in range(len(D)) if sub>>i&1)
                R=G.power(G.indicator(S),2)
                if R in seen: injective=False
                seen.add(R); domain_functions+=1
            require(injective==expected,'iff criterion on allowed domain')
            domains+=1; injective_domains+=expected
    digit_rows=[]; digit_total=0
    for p,max_n in ((3,7),(5,5)):
        for n in range(1,max_n+1):
            G=FiniteAbelianGroup((n,)); count=0
            for f in product(range(p),repeat=n):
                R=G.power(f,p)
                require(tuple(v%p for v in R)==tuple(v%p for v in G.push(f,p)),'prime Frobenius')
                if gcd(n,p)==1:
                    require(decode_digit_power(G,R,p,range(n))['candidate']==list(f),'digit recovery')
                count+=1; digit_total+=1
            digit_rows.append({'n':n,'p':p,'digit_vectors':count})
    prod_rows=[]; prod_total=0
    for moduli in ((2,2),(2,3),(2,4),(3,3)):
        G=FiniteAbelianGroup(moduli)
        for p in (2,3):
            image=G.multiply(p); reps={}
            for i,j in enumerate(image): reps.setdefault(j,i)
            D=tuple(reps.values()); count=0
            for mask in range(1<<G.n):
                f=G.indicator(G.support(mask)); R=G.power(f,p)
                require(tuple(v%p for v in R)==tuple(v%p for v in G.push(f,p)),'product-group Frobenius')
                prod_total+=1; count+=1
            for mask in range(1<<len(D)):
                f=G.indicator(tuple(D[i] for i in range(len(D)) if mask>>i&1))
                require(decode_digit_power(G,G.power(f,p),p,D)['candidate']==list(f),'product transversal')
            prod_rows.append({'moduli':list(moduli),'p':p,'binary_vectors':count,
                              'transversal_size':len(D),'transversal_vectors':1<<len(D)})
    # Prime-power iteration, independent of ordinary p-power test above.
    pp_checks=0
    for p,k,maxn in ((2,2,8),(3,2,5)):
        for n in range(1,maxn+1):
            G=FiniteAbelianGroup((n,)); m=p**k
            for mask in range(1<<n):
                f=G.indicator(G.support(mask)); R=G.power(f,m)
                require(tuple(v%p for v in R)==tuple(v%p for v in G.push(f,m)),'iterated Frobenius')
                if gcd(n,p)==1: require(decode_digit_power(G,R,p,range(n),k)['candidate']==list(f),'iterated recovery')
                pp_checks+=1
    weights=(0,1,2),(2,1,0); G3=FiniteAbelianGroup((3,))
    require(G3.power(weights[0],2)==G3.power(weights[1],2),'weighted odd counterexample')
    G5=FiniteAbelianGroup((5,)); invalid=[0,0,0,0,2]
    require(decode_digit_power(G5,invalid,2,range(5))['status']=='inconsistent_data','full-data recheck')
    nonabelian=s3_control(); require(nonabelian['frobenius_mod2_fails'],'S3 control')
    examples=[verify_collision(6,(0,1,2),(3,4,5)),verify_collision(6,(0,1,4),(0,2,5))]
    return {'status':'PASS','study':'PAPP-MATH-REPAIR-LAB-03',
        'claims':'Finite arithmetic coverage only. Written general proofs are separate. No PAPP behavior measured.',
        'cyclic_binary':{'range':[2,14],'supports':total,'odd_reconstructions':odd,'even_parity_checks':even,'rows':rows},
        'allowed_domains_binary':{'range':[2,10],'domains':domains,'support_domain_pairs':domain_functions,'injective_domains':injective_domains,'all_iff_checks_pass':True},
        'digit_prime_power':{'vectors':digit_total,'rows':digit_rows},
        'noncyclic_products':{'binary_vectors':prod_total,'rows':prod_rows},
        'iterated_prime_power_binary_checks':pp_checks,
        'known_witnesses':examples,
        'exploratory_collision_atlas':{'searched_cyclic_orders':[2,14], 'first_found_by_loop_order_not_claimed_globally_minimal':atlas},
        'weighted_odd_counterexample':{'n':3,'f':list(weights[0]),'g':list(weights[1]),'square':list(G3.power(weights[0],2))},
        'nonabelian_control':nonabelian,
        'invalid_observation_control':decode_digit_power(G5,invalid,2,range(5)),
        'not_run':['model comparison','blind trial','independent human review','Lean','FCIG audit']}

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--output',type=Path,default=ROOT/'results/exact_results.json')
    args=parser.parse_args()
    try:
        result=run(); args.output.parent.mkdir(parents=True,exist_ok=True)
        data=(json.dumps(result,indent=2,sort_keys=True)+'\n').encode()
        args.output.write_bytes(data)
        print(json.dumps({'status':result['status'],'output':str(args.output),'sha256':hashlib.sha256(data).hexdigest(),'cyclic_supports':result['cyclic_binary']['supports'],'digit_vectors':result['digit_prime_power']['vectors'],'domain_support_pairs':result['allowed_domains_binary']['support_domain_pairs']},indent=2))
    except Exception as exc:
        print(f'FAILED: {exc}',file=sys.stderr);sys.exit(1)
