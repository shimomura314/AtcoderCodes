def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))

    ans = m*n-sum(a)
    if ans > k:
        print(-1)
        return
    if ans < 0:
        ans = 0
    print(ans)


if __name__ == "__main__":
    main()