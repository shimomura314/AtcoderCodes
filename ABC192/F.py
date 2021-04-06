def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    answer = 10**20
    for k in range(1, n+1):
        mod = [[[-1 for _ in range(k)] for _ in range(k+1)] for _ in range(n+1)]
        mod[0][0][0] = 0
        for i in range(n):
            for j in range(k,-1,-1):
                for m in range(k):
                    mod[i+1][j][m] = mod[i][j][m]
            for j in range(k-1,-1,-1):
                for m in range(k):
                    if mod[i][j][m] != -1:
                        mod[i+1][j+1][(m+a[i])%k] = max(mod[i+1][j+1][(m+a[i])%k], mod[i][j][m] + a[i])
        if mod[n][k][x%k] != -1:
            answer = min(answer, int((x-mod[n][k][x%k])//k))
    print(answer)


if __name__ == "__main__":
    main()