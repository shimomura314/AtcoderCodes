import sys
input = sys.stdin.readline
mod = 10**9 + 7
sys.setrecursionlimit(10 ** 8)


def f(x,y):
    if x < 0 or h <= x or y < 0 or w <= y:
        return 0
    if s[x][y] != 0:
        return s[x][y]
    dx = (1,0,-1,0)
    dy = (0,1,0,-1)
    s[x][y] = 1
    for i in range(4):
        sx = x + dx[i]
        sy = y + dy[i]
        if 0 <= sx < h and 0 <= sy < w and 0 <= x < h and 0 <= y < w and a[x][y] < a[sx][sy]:
            s[x][y] += f(sx,sy)
            s[x][y] %= mod
    return s[x][y]


h,w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]
ans = 0
s = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        ans += f(i,j)
        ans %= mod
print(ans)