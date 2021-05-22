from heapq import heappop, heappush


def dijkstra(s,n,g):
    que = []
    d = [10**15 for _ in range(n)]
    d[s] = 0
    heappush( que,(0,s) )
    while que:
        p =  heappop(que)
        v = p[1]
        if d[v] < p[0]:
            continue
        for i in range(len(g[v])):
            edge = g[v][i]
            if d[edge[0]] > d[v] + edge[1]:
                d[edge[0]] = d[v] + edge[1]
                heappush( que,(d[edge[0]] , edge[0]) )
    return d


def main():
    n,m,t = map(int,input().split())
    money = list(map(int,input().split()))
    g1 = [[] for _ in range(n)]
    g2 = [[] for _ in range(n)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        a -= 1
        b -= 1
        g1[a].append((b,c))
        g2[b].append((a,c))
    d1 = dijkstra(0,n,g1)
    d2 = dijkstra(0,n,g2)
    ans = 0
    for i in range(n):
        ans = max(ans,(t-(d1[i]+d2[i]))*money[i])
    print(ans)


if __name__ == "__main__":
    main()