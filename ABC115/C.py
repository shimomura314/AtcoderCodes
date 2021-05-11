n,k = map(int,input().split())
h = [0 for _ in range(n)]
for i in range(n):
    h[i] = int(input())
h.sort()
m = sum(h)
for i in range(n-k+1):
    m = min(h[i+k-1]-h[i], m)
print(m)