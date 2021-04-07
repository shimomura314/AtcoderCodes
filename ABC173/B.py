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
    n = int(input())
    dic = defaultdict(int)
    for _ in range(n):
        dic[input()] += 1

    print('AC x', dic['AC'])
    print('WA x', dic['WA'])
    print('TLE x', dic['TLE'])
    print('RE x', dic['RE'])


if __name__ == "__main__":
    main()