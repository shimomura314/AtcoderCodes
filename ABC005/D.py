import sys, bisect, copy
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def f(xu,yl,xd,yr,sumation,flag):
    global dp,d,dpx,dpy,past
    n = len(d)
    if xu == xd or yl == yr or xd > n or yr > n:
        return
    if past[xu][yl][xd][yr]:
        return
    past[xu][yl][xd][yr] = 1
    if flag == 1:
        sumation -= dpx[xu-1][yr] - dpx[xu-1][yl]
    if flag == 2:
        sumation -= dpy[yl-1][xd] - dpy[yl-1][xu]
    if flag == 3:
        sumation += dpx[xd-1][yr] - dpx[xd-1][yl]
    if flag == 4:
        sumation += dpy[yr-1][xd] - dpy[yr-1][xu]
    dp[(xd-xu)*(yr-yl)] = max(dp[(xd-xu)*(yr-yl)],sumation)
    f(xu+1, yl, xd, yr, sumation, 1)
    f(xu, yl+1, xd, yr, sumation, 2)
    f(xu, yl, xd+1, yr, sumation, 3)
    f(xu, yl, xd, yr+1, sumation, 4)

def main ():
    global dp,d,dpx,dpy,past
    n = int(input())
    d = [list(map(int,input().split())) for _ in range(n)]
    dp = [0 for _ in range(n**2+1)]
    dpx = [[0 for _ in range(n+1)] for _ in range(n)]
    dpy = [[0 for _ in range(n+1)] for _ in range(n)]
    past = [[[[0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            dpx[i][j+1] = dpx[i][j] + d[i][j]
    for j in range(n):
        for i in range(n):
            dpy[j][i+1] = dpy[j][i] + d[i][j]

    f(0,0,1,1,d[0][0],0)

    for i in range(n**2):
        dp[i+1] = max(dp[i],dp[i+1])
    q = int(input())
    for _ in range(q):
        p = int(input())
        print(dp[p])


if __name__ == "__main__":
    main()