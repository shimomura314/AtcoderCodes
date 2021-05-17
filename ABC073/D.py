from itertools import permutations


def main():
    n,m,r = map(int,input().split())
    R = list(map(int,input().split()))
    d = [[10**10 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        x,y,z = map(int,input().split())
        x -= 1
        y -= 1
        d[x][y] = z
        d[y][x] = z
    for i in range(n):
        d[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    ans = float('inf')
    for com in permutations(R, r):
        temp = 0
        for i in range(r-1):
            temp += d[com[i]-1][com[i+1]-1]
        ans = min(ans, temp)
    print(ans)


if __name__ == "__main__":
    main()