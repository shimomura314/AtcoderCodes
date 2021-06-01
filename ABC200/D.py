import copy
import sys


def main():
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(n):
        a[i] = a[i]%200
    dp = [[[] for _ in range(200)] for _ in range(n+1)]
    dp[0][0] = [0]
    for i in range(n):
        for j in range(200):
            if dp[i][j] == []:
                continue
            dp[i+1][j] = copy.deepcopy(dp[i][j])
        for j in range(200):
            if dp[i][j] == []:
                continue
            if dp[i+1][(j+a[i])%200] == []:
                dp[i+1][(j+a[i])%200] = copy.deepcopy(dp[i][j])
                dp[i+1][(j+a[i])%200].append(i+1)
            else:
                if dp[i+1][(j+a[i])%200] == [0]:
                    dp[i+1][(j+a[i])%200] = [0, i+1]
                    continue
                print("Yes")
                b = dp[i][j]
                b.append(i+1)
                c = dp[i+1][(j+a[i])%200]
                b[0] = len(b)-1
                c[0] = len(c)-1
                print(*b)
                print(*c)
                return
    print("No")


if __name__ == "__main__":
    main()