import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7


def main():
    r,c,k = map(int,input().split())
    n = int(input())
    rc = []
    R = [0 for _ in range(r)]
    C = [0 for _ in range(c)]
    for _ in range(n):
        x,y = map(int,input().split())
        x -= 1
        y -= 1
        R[x] += 1
        C[y] += 1
        rc.append((x,y))
    
    R_count = defaultdict(int)
    C_count = defaultdict(int)
    for i in range(r):
        if R[i] <= k+1:
            R_count[R[i]] += 1
    for i in range(c):
        if C[i] <= k+1:
            C_count[C[i]] += 1
    
    answer = 0
    for i in range(k+1):
        answer += R_count[i] * C_count[k-i]
    for i in range(n):
        [r,c] = rc[i]
        if R[r] + C[c] == k+1:
            answer += 1
        if R[r] + C[c] == k:
            answer -= 1
    print(answer)


if __name__ == "__main__":
    main()