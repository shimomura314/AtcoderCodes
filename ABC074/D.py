import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def main():
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(n)]
    g = [[] for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1,n):
            g[i].append((j, a[i][j]))
            g[j].append((i, a[i][j]))
    answer = 0
    for i in range(n):
        answer += sum(a[i])
    answer //= 2
    w = []
    for i in range(n):
        que = []
        d = [10**15 for _ in range(n)]
        d[i] = 0
        heappush( que,(0,i) )
        while que:
            p =  heappop(que)
            v = p[1]
            if d[v] < p[0]:
                continue
            for k in range(len(g[v])):
                edge = g[v][k]
                if d[edge[0]] > d[v] + edge[1]:
                    d[edge[0]] = d[v] + edge[1]
                    heappush( que,(d[edge[0]] , edge[0]) )
        w.append(d)
    for i in range(n-1):
        for j in range(i+1,n):
            if w[i][j] < a[i][j]:
                print(-1)
                return
            flag = 0
            for k in range(n):
                if i == k or j == k:
                    continue
                if w[i][k] + w[k][j] == w[i][j]:
                    flag = 1
            if flag:
                answer -= w[i][j]
    print(answer)


if __name__ == "__main__":
    main()