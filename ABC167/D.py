import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
from fractions import gcd


def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    past = [0 for _ in range(n)]
    past[0] = 1
    root = [0]
    pre = 0
    while True:
        Next = a[pre]-1
        if past[Next]:
            break
        root.append(Next)
        pre = Next
        past[Next] = 1

    rev = []
    i = 0
    while root[len(root)-1-i] != Next:
        rev.append(root[len(root)-1-i])
        i += 1
    rev.reverse()
    rever = [Next]
    for i in range(len(rev)):
        rever.append(rev[i])
    n1 = len(root)
    n2 = len(rever)
    if n1-1 >= k:
        print(root[k]+1)
        return
    if rever[0] != 0:
        k -= n1-n2
    print(rever[(k)%n2] + 1)


if __name__ == "__main__":
    main()