def rotation_find(n,m,g): # 迷路を外側からぐるぐると探索 
    did = [[False for _ in range(m+2)] for _ in range(n+2)]
    for i in range(n+2):
        did[i][0] = True
        did[i][m+1] = True
    for i in range(m+2):
        did[0][i] = True
        did[n+1][i] = True
    x = 1
    y = 1
    key = 1
    ans = []
    while True:
        did[x][y] = True
        key1 = 0
        if g[x-1][y-1]%2 != 0:
            key1 = 1
        a,b = x,y
        if key == 1:
            x += 1
        elif key == 2:
            y += 1
        elif key == 3:
            x -= 1
        elif key == 4:
            y -= 1
        if key == 1 and did[x][y]:
            x -= 1
            y += 1
            key=2
        elif key == 2 and did[x][y]:
            y -= 1
            x -= 1
            key=3
        elif key == 3 and did[x][y]:
            x += 1
            y -= 1
            key=4
        elif key == 4 and did[x][y]:
            x += 1
            y += 1
            key=1
        if did[x][y]:
            break
        if key1:
            g[a-1][b-1] -= 1
            g[x-1][y-1] += 1
            ans.append((a,b,x,y))
    return ans


def main():
    h,w = map(int,input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = rotation_find(h,w,a)
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])


if __name__ == "__main__":
    main()