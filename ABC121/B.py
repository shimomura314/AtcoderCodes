n,m,c = map(int,input().split())
b = list(map(int,input().split()))
a = [0 for i in range(n)]
for i in range(n):
    a[i] = list(map(int,input().split()))

count = 0
for i in range(n):
    sumation = 0
    for j in range(m):
        sumation += b[j]*a[i][j]
    sumation += c
    if(sumation > 0):
        count += 1

print(count)