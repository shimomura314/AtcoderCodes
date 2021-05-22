import sys
from itertools import combinations
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def main():
    n,W = map(int,input().split())
    w = []
    v = []
    for _ in range(n):
        a,b = map(int,input().split())
        v.append(a)
        w.append(b)
    if max(w) <= 1000:
        dp  =[[0 for _ in range(W+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(W+1):
                dp[i][j] = max( dp[i][j],dp[i-1][j] )
                if j >= w[i-1]:
                    dp[i][j] = max(dp[i][j],dp[i-1][j-w[i-1]]+v[i-1])
        print(max(dp[n]))
        return
    elif max(v) <= 1000:
        v_max = max(v)*n
        dp = [10**20 for _ in range(v_max+1)]
        dp[0] = 0
        for i in range(n):
            for j in range(v_max,v[i]-1,-1):
                dp[j] = min(dp[j],dp[j-v[i]]+w[i])
        ans=0
        for i in range(v_max+1):
            if dp[i] <= W:
                ans = i
        print(ans)
        return
    A = []
    B = []
    for i in range(n):
        if i <= n//2:
            A.append((w[i],v[i]))
        else:
            B.append((w[i],v[i]))
    A_select = []
    B_select = []
    for num in range(0, len(A)+1):
        for e in combinations(range(len(A)),num):
            weight = 0
            value = 0
            for x in e:
                weight += A[x][0]
                value += A[x][1]
            A_select.append((weight,value))
    for num in range(0,len(B)+1):
        for e in combinations(range(len(B)),num):
            weight = 0
            value = 0
            for x in e:
                weight += B[x][0]
                value += B[x][1]
            B_select.append((weight,value))
    A_select.sort()
    max_value = 0
    A_true = []
    for i in range(len(A_select)):
        if A_select[i][1] < max_value:
            continue
        max_value = max(max_value,A_select[i][1])
        A_true.append(A_select[i])
    ans = 0
    for e in B_select:
        if e[0] > W:
            continue
        ok = 0
        ng = len(A_true)
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if e[0] + A_true[mid][0] <= W:
                ok = mid
            else:
                ng = mid
        ans = max(ans, e[1]+A_true[ok][1])
    print(ans)


if __name__ == "__main__":
    main()