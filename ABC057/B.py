n,m = map(int,input().split())
a = [0 for _ in range(n)]
b = [0 for _ in range(n)]
c = [0 for _ in range(m)]
d = [0 for _ in range(m)]
for i in range(n):
    a[i],b[i] = map(int,input().split())
for i in range(m):
    c[i],d[i] = map(int,input().split())
for i in range(n):
    ans = 0
    temp = float('inf')
    for j in range(m):
        if temp > abs(a[i]-c[j]) + abs(b[i]-d[j]):
            ans = j+1
            temp = abs(a[i]-c[j]) + abs(b[i]-d[j])
    print(ans)