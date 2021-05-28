def main():
    w = int(input())
    n,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    dp = [[w+1 for _ in range(100*n+1)] for _ in range(k+1)]
    dp[0][0] = 0
    for i in range(n):
        for x in range(min(i,k-1), -1, -1):
            for y in range(ab[i][1], 100*n+1):
                dp[x+1][y] = min(dp[x+1][y],dp[x][y-ab[i][1]] + ab[i][0])
    answer = 0
    for i in range(k+1):
        for j in range(100*n, -1, -1):
            if dp[i][j] <= w:
                answer = max(answer,j)
                break
    print(answer)


if __name__ == "__main__":
    main()