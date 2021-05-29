import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def main():
    n,d = map(int,input().split())
    x,y = map(int,input().split())
    n += 1
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    n -= 1
    if x%d != 0 or y%d != 0:
        print(0)
        return
    x = abs(x)
    y = abs(y)
    minx = x//d
    miny = y//d
    if (n - minx - miny) % 2 != 0:
        print(0)
        return
    ans = 0
    for n1 in range(minx, n-miny+1, 2):
        n2 = n - n1
        cnt = 1
        e1 = (n1 + minx) // 2
        e2 = (n1 - minx) // 2
        e3 = (n2 + miny) // 2
        e4 = (n2 - miny) // 2
        cnt *= dp[n+1][e1+1] / pow(4,e1)
        cnt *= dp[n-e1+1][e2+1] / pow(4,e2)
        cnt *= dp[n-e1-e2+1][e3+1] / pow(4,e3)
        ans += cnt / pow(4,e4)
    print(ans)


if __name__ == "__main__":
    main()