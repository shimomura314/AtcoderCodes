from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def main():
    n = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        a,b,w = map(int,input().split())
        a -= 1
        b -= 1
        graph[a].append((b,w))
        graph[b].append((a,w))
    q,k = map(int,input().split())
    que = deque([k-1])
    dis = [-1 for _ in range(n)]
    dis[k-1] = 0
    while que:
        node = que.pop()
        for next_node, distance in graph[node]:
            if dis[next_node] == -1:
                dis[next_node] = dis[node] + distance
                que.append(next_node)
    for _ in range(q):
        x,y = map(int,input().split())
        print( dis[x-1] + dis[y-1] ) 


if __name__ == "__main__":
    main()