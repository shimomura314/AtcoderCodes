n = int(input())
a = list(map(int,input().split())) 
cnt = 0
for i in range(n):
    if a[i] != 0:
        cnt += 1
answer = sum(a)//cnt
if sum(a)%cnt != 0:
    answer += 1
print(answer)