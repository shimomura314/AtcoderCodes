n = int(input())
g = [[] for _ in range(n)]
chi = [0 for _ in range(n)]
for i in range(n-1):
    b = int(input())
    g[b-1].append(i+1)
    chi[b-1] += 1
point = [1 for _ in range(n)]
for i in range(n-1,-1,-1):
    if len(g[i])>0:
        m = 10**18
        M = 0
        for e in g[i]:
            m = min(m, point[e])
            M = max(M, point[e])
        point[i] = m+M+1
print(point[0])