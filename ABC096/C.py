def main():
    n,m = map(int,input().split())
    maze = []
    for _ in range(n):
        maze.append(list(input()))
    for i in range(n):
        for j in range(m):
            if maze[i][j] == "#":
                if  (j != 0 and maze[i][j-1] == "#") or (j != m-1 and maze[i][j+1] == "#") or\
                    (i != 0 and maze[i-1][j] == "#") or (i != n-1 and maze[i+1][j] == "#"):
                    continue
                else:
                    print("No")
                    return
    print("Yes")


if __name__ == "__main__":
    main()