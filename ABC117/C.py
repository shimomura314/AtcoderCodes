n,m = map(int,input().split())
x = list(map(int,input().split()))
if n >= m:
    print(0)
    exit()

x.sort()
y = [0 for _ in range(len(x)-1)]
for i in range(len(x)-1):
    y[i] = x[i+1]-x[i]
y.sort(reverse=True)
answer = 0
for i in range(n-1):
    answer += y[i]
print( max(x)-min(x)-answer )