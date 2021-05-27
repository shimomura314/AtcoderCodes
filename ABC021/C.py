import sys
sys.setrecursionlimit(10**8)
mod = 10**9+7


def main():
    n = int(input())
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    m = int(input())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        g[b].append(a)
        g[a].append(b)
    
    ans = [0 for _ in range(n)]
    did = [False for _ in range(n)]
    ans[x] = 1
    did[x] = True
    que = [x]
    while que:
        tank = []
        for nex in que:
            for go in g[nex]:
                if did[go]:
                    continue
                ans[go] = (ans[go]+ans[nex])%mod
        for nex in que:
            for go in g[nex]:
                if did[go]:
                    continue
                tank.append(go)
                did[go]=True
        que = tank
        if ans[y]!=0:
            print(ans[y])
            return


if __name__ == "__main__":
    main()