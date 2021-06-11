n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
N = max(a)+1
tab = [1 for _ in range(N)]
for i in range(n):
    x = a[i]
    if i < n-1 and a[i] == a[i+1]:
        tab[a[i]] = 0
    if tab[x]:
        ans += 1
    for i in range(N):
        if x*i >= N:
            break
        tab[x*i] = 0        
print(ans)