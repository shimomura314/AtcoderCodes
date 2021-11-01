h, w, x, y = map(int, input().split())
s = [list(input()) for _ in range(h)]

visible = 1
dxy = ((0, 1), (0, -1), (1, 0), (-1, 0))
for dx, dy in dxy:
    sx, sy = x-1, y-1
    while True:
        sx += dx
        sy += dy
        if 0 <= sx < h and 0 <= sy < w and s[sx][sy] == ".":
            visible += 1
        else:
            break
print(visible)
