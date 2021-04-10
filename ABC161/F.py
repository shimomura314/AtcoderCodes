import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
from fractions import gcd
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

def f(x, k, ans):
    if x < k:
        if x == 1:
            ans.append(k)
        return
    if x%k == 0:
        while x%k == 0:
            x //= k
        f(x, k, ans)
    else:
        f(x%k, k, ans)
    return


def divisor(x):
    divisors = []
    for integer in range(1, int(x**0.5)+1):
        if(x%integer == 0):
            divisors.append(integer)
            divisors.append(x//integer)
    for integer in range(1, int((x+1)**0.5)+1):
        if((x+1)%integer == 0):
            divisors.append(integer)
            divisors.append((x+1)//integer)

    divisors = list(set(divisors))
    divisors.sort()
    return divisors


def main():
    ans = []
    n = inp()
    divisors = divisor(n-1)
    for e in divisors:
        if e == 1:
            continue
        f(n,e,ans)
    print(len(ans))


if __name__ == "__main__":
    main()