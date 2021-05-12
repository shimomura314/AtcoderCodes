def dfs(s, n):
    if int(s) > n:
        return 0
    ret = 1 if all(s.count(c) > 0 for c in '753') else 0
    for c in '753':
        ret += dfs(s + c, n)
    return ret


def main():
    n = int(input())
    print(dfs('0', n))


if __name__ == "__main__":
    main()