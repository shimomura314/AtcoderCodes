N = list(input())
n = int("".join(N))
ans = 0
for i in range(len(N)):
    span = 10**(i+1)
    x,y = n//span, n%span
    ans += x*span//10
    if y:
        ans += min(max(0, (y-(10**i-1))), span//10)
print(ans)