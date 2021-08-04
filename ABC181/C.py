from itertools import combinations

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

for pair in combinations(xy, 3):
    dx1, dy1 = pair[0][0]-pair[1][0], pair[0][1]-pair[1][1]
    dx2, dy2 = pair[0][0]-pair[2][0], pair[0][1]-pair[2][1]
    if dx1*dy2 == dx2*dy1:
        print("Yes")
        exit()
print("No")
