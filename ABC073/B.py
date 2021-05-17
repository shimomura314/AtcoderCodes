n = int(input())
answer = 0
for _ in range(n):
    x,y = map(int,input().split())
    answer += y-x+1
print(answer)