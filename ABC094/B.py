n,m,x = map(int,input().split())
a = list(map(int,input().split()))
R = 0

for i in range(m):
    if a[i] > x:
        R += 1

print(min(m-R,R))