def dfs(n, s):
    if len(s) > n:
        return 0
    if len(s)==n:
        print(s)
    for c in 'abc':
        dfs(n, s+c)


def main():
    n = int(input())
    dfs(n, "")


if __name__ == "__main__":
    main()
