import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def main():
    n,m,x,y = map(int,input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a,b,t,k = map(int,input().split())
        graph[a-1].append((b-1, t, k))
        graph[b-1].append((a-1, t, k))
    x -= 1
    y -= 1

    que = deque([])
    time = [-1 for _ in range(n)]
    que.append(x)
    time[x] = 0
    while que:
        now = que.pop()
        for e in graph[now]:
            [to, T, K] = e
            comeTime = K - time[now]%K
            if time[now]%K == 0:
                comeTime = 0
            goTime = time[now] + comeTime + T
            if goTime < time[to] or time[to] == -1:
                time[to] = goTime
                que.append(to)
    print(time[y])


if __name__ == "__main__":
    main()