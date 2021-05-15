def main():
    n = int(input())
    dp = [10**10 for _ in range(n+1)]
    dp[0] = 0
    for coin in [
        1, 
        6, 6**2, 6**3, 6**4, 6**5, 6**6,
        9, 9**2, 9**3, 9**4, 9**5, 9**6
        ]:
        for i in range(n+1):
            if n < i+coin:
                continue
            dp[i+coin] = min(dp[i+coin], dp[i]+1)
    print(dp[n])


if __name__ == "__main__":
    main()