n = int(input())
a = list(map(int,input().split()))
answer = 0
pre = a[0]
for i in range(1,n):
    if a[i] < pre:
        answer += pre-a[i]
    else:
        pre = a[i]
print(answer)