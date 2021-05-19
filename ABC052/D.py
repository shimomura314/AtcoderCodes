n,a,b = map(int,input().split())
x = list(map(int,input().split()))
answer = 0
for i in range(1, n):
    if a*(x[i]-x[i-1]) < b:
        answer += a*(x[i]-x[i-1])
    else:
        answer += b
print(answer)