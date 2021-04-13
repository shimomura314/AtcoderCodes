def main():
    h,w = map(int,input().split())
    
    maze = []
    for _ in range(h):
        s = list(input())
        maze.append(s)
    ans = 0
    dx = [ 1, 0,-1, 0]
    dy = [ 0, 1, 0,-1]
    key = 0
    for sx in range(h):
        for sy in range(w):
            if maze[sx][sy] == '#':
                continue
            else:
                d = [[-1 for _ in range(w)] for _ in range(h)]
                que = []
                d[sx][sy] = 0
                que.append([sx,sy])
                M = 0
                while que:
                    [qx,qy]=que[0]
                    que.pop(0)
                    for i in range(4):
                        nx=qx+dx[i]
                        ny=qy+dy[i]
                        if nx >= 0 and h > nx and ny >= 0 and w > ny and maze[nx][ny] == "." and d[nx][ny] == -1:
                            d[nx][ny]=d[qx][qy]+1
                            if d[qx][qy]+1 > M:
                                M = d[qx][qy]+1
                            que.append([nx,ny])
                ans = max(ans,M)
    print(ans)


if __name__ == "__main__":
    main()