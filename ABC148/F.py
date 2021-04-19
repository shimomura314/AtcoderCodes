from collections import deque


def bfs(s, n, g):
    went = [False]*n
    dis = [0]*n
    que = deque([])
    que.append(s)
    went[s] = True
    while que:
        go = que.pop()
        for i in range(len(g[go])):
            if went[g[go][i]]:
                continue
            dis[g[go][i]] = dis[go] + 1
            went[g[go][i]] = True
            que.append(g[go][i])
    return dis


def main():
    n,u,v = map(int,input().split())
    
    g = [[] for _ in range(n)]
    g1 = [[] for _ in range(n)]
    ab = []
    for _ in range(n-1):
        a,b = map(int,input().split())
        
        a -= 1
        b -= 1
        g[b].append(a)
        g[a].append(b)
        ab.append((a,b))
    dis = bfs(u-1,n,g)
    path = [v-1]
    que = deque([])
    que.append(v-1)
    d = dis[v-1]-1
    while que:
        go = que.pop()
        for i in range(len(g[go])):
            if dis[g[go][i]] == d:
                d -= 1
                path.append(g[go][i])
                que.append(g[go][i])
    answer = int(len(path)/2)-1
    path.reverse()
    for i in range(n-1):
        if (ab[i][0], ab[i][1]) == (path[answer], path[answer+1]) or (ab[i][1], ab[i][0]) == (path[answer], path[answer+1]):
            continue
        g1[ab[i][0]].append(ab[i][1])
        g1[ab[i][1]].append(ab[i][0])
    dis1 = bfs(path[answer],n,g1)
    x = answer+max(dis1)
    if len(path)%2 == 1:
        x += 1
    print(x)




if __name__ == "__main__":
    main()