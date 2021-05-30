n,k = map(int,input().split())
ans = 0
for i in range(1, n+1):
    ans += 100*i*k
ans += ( k*(k+1)//2 ) * n
print(ans)