h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

answer = 0
for i in range(h-1):
    for j in range(w-1):
        black = 0
        if s[i][j] == "#":
            black += 1
        if s[i+1][j] == "#":
            black += 1
        if s[i][j+1] == "#":
            black += 1
        if s[i+1][j+1] == "#":
            black += 1
        if black == 1 or black == 3:
            answer += 1
print(answer)