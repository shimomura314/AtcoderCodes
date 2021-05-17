n = int(input())
k = int(input())
x = list(map(int,input().split()))
answer = 0
for i in range(n):
    answer += min(k-x[i], x[i])*2

print(answer)