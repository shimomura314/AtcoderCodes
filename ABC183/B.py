sx, sy, gx, gy = map(int, input().split())
if sx == gx:
    print(sx)
    exit()
print(sx + sy*(gx-sx)/(gy+sy))
