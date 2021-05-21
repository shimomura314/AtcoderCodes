def flogDP(n,k,h):
    dp = [float('inf') for _ in range(n)]
    dp[0] = 0
    for i in range(1,n):
        for j in range(max(0,i-k), i):
            dp[i] = min(dp[i], dp[j]+abs(h[i]-h[j]))
    print(dp[n-1])


def main():
    n = int(input())
    a = list(map(int,input().split()))
    flogDP(n, 2, a)


if __name__ == "__main__":
    main()
