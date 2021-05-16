def main():
    h,w = map(int,input().split())
    maze = []
    for _ in range(h):
        maze.append(list(input()))

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    que = []
    que.append([0,0])
    d = [[-1 for _ in range(w)] for _ in range(h)]
    d[0][0] = 0
    while len(que)!=0:
        qx,qy = que.pop()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] == "." and d[nx][ny] == -1:
                d[nx][ny] = d[qx][qy] + 1
                que.append([nx,ny])

    if d[h-1][w-1] == -1:
        print(-1)
        return
    cnt = 0
    for i in range(h):
        for j in range(w):
            if maze[i][j] == ".":
                cnt += 1
    print(cnt-d[h-1][w-1]-1)


if __name__ == "__main__":
    main()