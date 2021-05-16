import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
# from scipy.sparse.csgraph import floyd_warshall
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations, combinations_with_replacement
from heapq import heappop, heappush, heapify
from fractions import gcd
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7


def main():
    n,k = map(int,input().split())
    if k == 0:
        print(n**2)
        return
    answer = 0
    # Case : a < b
    answer += (n-k+1)*(n-k) // 2
    # Case : a > b
    for b in range(k, n):
        answer += (n//b - 1) * (b-k) 
        answer += max(0, n%b - k + 1)
    print(answer)


if __name__ == "__main__":
    main()