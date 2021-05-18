import sys
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7


def prim(n,g):
    edgelist = []
    used = [False for _ in range(n)]
    for edge in g[0]:
        heappush( edgelist, edge)
    used[0] = True
    res = 0 

    while len(edgelist)>0:
        minedge = heappop(edgelist)
        if used[minedge[1]]:
            continue
        v = minedge[1]
        used[v] = True
        for edge in g[v]:
            if not used[edge[1]]:
                heappush( edgelist, edge)
        res += minedge[0]
    return res

def main():
    n = int(input())
    xy = []
    for index in range(n):
        x,y = map(int,input().split())
        xy.append((x,y,index))
    
    g = [[] for _ in range(n)]
    xy.sort()
    for i in range(n-1):
        j = i+1
        w = min(abs(xy[i][0]-xy[j][0]),abs(xy[i][1]-xy[j][1]))
        a = xy[i][2]
        b = xy[j][2]
        g[a].append((w,b))
        g[b].append((w,a))
    xy.sort(key=lambda y:y[1])
    for i in range(n-1):
        j = i+1
        w = min(abs(xy[i][0]-xy[j][0]),abs(xy[i][1]-xy[j][1]))
        a = xy[i][2]
        b = xy[j][2]
        g[a].append((w,b))
        g[b].append((w,a))
    print( prim(n, g) )


if __name__ == "__main__":
    main()