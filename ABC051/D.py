def main():
    n,w = map(int,input().split())
    d = [[10**10 for _ in range(n)] for _ in range(n)] 
    edge = []
    for _ in range(w):
        x,y,z = map(int,input().split())
        x -= 1
        y -= 1
        edge.append((x,y,z))
        d[x][y] = z
        d[y][x] = z
    for i in range(n):
        d[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    
    count = 0
    for x,y,z in edge:
        flag = False
        for j in range(n):
            if d[j][x] + z == d[j][y]:
                flag = True
                break
            if d[j][y] + z == d[j][x]:
                flag = True
                break
        if not flag:
            count += 1
    print(count)


if __name__ == "__main__":
    main()