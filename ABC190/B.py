n, s, d = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]
for x, y in xy:
    if x >= s or y <= d:
        continue
    print("Yes")
    exit()
print("No")