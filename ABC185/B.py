n, m, t = map(int, input().split())
max_N = n
pre = 0
for _ in range(m):
    a, b = map(int, input().split())
    n -= a-pre
    if n <= 0:
        print("No")
        exit()
    n += b-a
    n = min(n, max_N)
    pre = b
if n > t-pre:
    print("Yes")
else:
    print("No")
