s = list(map(int,input().split()))
s.sort()
ans = 1
if s[0] != s[1]:
    ans += 1
if s[1] != s[2]:
    ans += 1
print(ans)