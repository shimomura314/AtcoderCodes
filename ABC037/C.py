n,k = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for i in range(n):
    ans += a[i]*min(k, i+1, n-i, n-k+1)
print(ans)