n = int(input())
pi = 3.141592653589
r = [int(input()) for _ in range(n)]
r.sort(reverse=True)
ans = 0
for i in range(n):
    if i%2 == 0:
        ans += r[i]*r[i]
    else:
        ans -= r[i]*r[i]
print(ans*pi)