n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
answer = 0
for i in range(n-1):
    for j in range(i+1, n):
        trend = (xy[i][1]-xy[j][1]) / (xy[i][0]-xy[j][0])
        if -1 <= trend <= 1:
            answer += 1
print(answer)